"""
Usage:
    Set
        export ICAV2_ACCESS_TOKEN=...
        export ICAV2_PROJECT_ID=...
    Then
        python get_activation_id.py
"""
import json
import os
from importlib.metadata import version

from libica.openapi.v3 import Configuration, ApiClient, EntitlementDetailApi, \
    SearchMatchingActivationCodesForCwlAnalysis, ApiException, CwlAnalysisJsonInput, CwlAnalysisInput

icav2_access_token = os.environ['ICAV2_ACCESS_TOKEN']
ica_url = "https://ica.illumina.com/ica/rest"

# Modify to suit your setting
project_id = "ea19a3f5-ec7c-4940-a474-c31cd91dbad4"
pipeline_id = "03689516-b7f8-4dca-bba9-8405b85fae45"


def get_activation_id(analysis_input) -> str:
    # Create an instance of the API class
    api_instance = EntitlementDetailApi(api_client)
    search_matching_activation_codes_for_cwl_analysis = SearchMatchingActivationCodesForCwlAnalysis(
        projectId=project_id,
        pipelineId=pipeline_id,
        analysisInput=analysis_input
    )

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search the best matching activation code detail for Cwl pipeline.
        api_response = api_instance.find_best_matching_activation_code_for_cwl(
            search_matching_activation_codes_for_cwl_analysis=search_matching_activation_codes_for_cwl_analysis
        )
    except ApiException as e:
        raise ValueError(
            "Exception when calling EntitlementDetailApi->find_best_matching_activation_code_for_cwl: %s\n" % e)

    return api_response.id


if __name__ == '__main__':
    print(f"libica-{version('libica')}")
    print("-" * 64)

    configuration = Configuration(
        host=ica_url,
        access_token=icav2_access_token,
    )
    # configuration.debug = True  # uncomment to debug API call logging

    api_client = ApiClient(configuration=configuration)

    cwl_analysis_json_input = CwlAnalysisJsonInput(
        objectType='JSON',  # STRUCTURED or JSON
        inputJson=json.dumps({}),
    )

    cwl_analysis_input = CwlAnalysisInput(cwl_analysis_json_input)

    activation_id = get_activation_id(analysis_input=cwl_analysis_input)

    print(f"activation_id: {activation_id}")
