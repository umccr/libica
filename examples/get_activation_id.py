import json
import os
from importlib.metadata import version

import libica
from libica.openapi.v2 import Configuration
from libica.openapi.v2.api import entitlement_detail_api
from libica.openapi.v2.model.cwl_analysis_json_input import CwlAnalysisJsonInput
from libica.openapi.v2.model.search_matching_activation_codes_for_cwl_analysis import \
    SearchMatchingActivationCodesForCwlAnalysis

icav2_access_token = os.environ['ICAV2_ACCESS_TOKEN']
ica_url = "https://ica.illumina.com/ica/rest"

configuration = Configuration(
    host=ica_url,
    access_token=icav2_access_token,
)


# configuration.debug = True  # uncomment to debug API call logging


def get_activation_id(project_id: str, pipeline_id: str, analysis_input) -> str:
    # Enter a context with an instance of the API client
    with libica.openapi.v2.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = entitlement_detail_api.EntitlementDetailApi(api_client)
        search_matching_activation_codes_for_cwl_analysis = SearchMatchingActivationCodesForCwlAnalysis(
            project_id=project_id,
            pipeline_id=pipeline_id,
            analysis_input=analysis_input,
        )  # SearchMatchingActivationCodesForCwlAnalysis |  (optional)

        # example passing only required values which don't have defaults set
        # and optional values
        try:
            # Search the best matching activation code detail for Cwl pipeline.
            api_response = api_instance.find_best_matching_activation_code_for_cwl(
                search_matching_activation_codes_for_cwl_analysis=search_matching_activation_codes_for_cwl_analysis
            )
        except libica.openapi.v2.ApiException as e:
            raise ValueError(
                "Exception when calling EntitlementDetailApi->find_best_matching_activation_code_for_cwl: %s\n" % e)

    return api_response.id


if __name__ == '__main__':
    print(f"libica-{version('libica')}")
    print("-" * 64)

    cwl_analysis_input = CwlAnalysisJsonInput(
        object_type='JSON',  # STRUCTURED or JSON
        input_json=json.dumps({}),
    )

    activation_id = get_activation_id(
        project_id='9c20aeb0-f780-4e9a-ac42-739b30ed91f3',
        pipeline_id='6358b7ca-a6c4-4a5a-be2e-899f18ebcdc5',
        analysis_input=cwl_analysis_input
    )

    print(f"activation_id: {activation_id}")
