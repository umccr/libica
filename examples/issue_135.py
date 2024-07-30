# Standard imports
from importlib.metadata import version
from os import environ

# Libica imports
from libica.openapi.v2 import ApiClient, Configuration
from libica.openapi.v2.api.project_analysis_api import ProjectAnalysisApi
from libica.openapi.v2.model.analysis_data_input import AnalysisDataInput
from libica.openapi.v2.model.analysis_output_mapping import AnalysisOutputMapping
from libica.openapi.v2.model.analysis_parameter_input import AnalysisParameterInput
from libica.openapi.v2.model.analysis_tag import AnalysisTag
from libica.openapi.v2.model.analysis_v3 import AnalysisV3
from libica.openapi.v2.model.analysis_v4 import AnalysisV4
from libica.openapi.v2.model.create_nextflow_analysis import CreateNextflowAnalysis
from libica.openapi.v2.model.nextflow_analysis_input import NextflowAnalysisInput

project_id = "7595e8f2-32d3-4c76-a324-c6a85dae87b5"  # trial project
pipeline_id = "fdef5902-3f50-4ee7-ae17-15d38d4b489c"

nextflow_analysis = CreateNextflowAnalysis(
    user_reference='PTC-ctTSO-v2-launch-test-vickie',
    pipeline_id=pipeline_id,
    tags=AnalysisTag(
        reference_tags=[],
        technical_tags=[
            'portal_run_id=20240308abcd6789'
        ],
        user_tags=[
            'subject_id=SBJ04405',
            'library_id=L2301368',
            'instrument_run_id=231116_A01052_0172_BHVLM5DSX7',  # pragma: allowlist secret
            'project_owner=UMCCR',
            'project_name=testing'
        ]
    ),
    analysis_input=NextflowAnalysisInput(
        inputs=[
            AnalysisDataInput(
                data_ids=['fol.58422302edd141213e0f08dc3cace45e'],
                parameter_code='run_folder'
            ),
            AnalysisDataInput(
                data_ids=['fil.94813f45b9e94977b0a308dc388cf24f'],
                parameter_code='sample_sheet'
            ),
        ],
        parameters=[
            AnalysisParameterInput(
                code="StartsFromFastq",
                value="true",
            ),
            AnalysisParameterInput(
                code="sample_pair_ids",
                multi_value=["L2301368"]
            )
        ],
        activation_code_detail_id='7f03a57e-2cfc-4b35-9cbb-d19e6ce9984b',
        analysis_storage_id='3fab13dd-46e7-4b54-bb34-b80a01a99379',
        analysis_output=[
            AnalysisOutputMapping(
                source_path='out/',
                target_path='/ilmn_cttso_fastq_cache/20240308abcd6789/',
                target_project_id='7595e8f2-32d3-4c76-a324-c6a85dae87b5',
                type='FOLDER'
            )
        ]
    )
)


def create_nextflow_analysis():
    configuration = Configuration(
        host=environ['ICAV2_BASE_URL'],
        access_token=environ['ICAV2_ACCESS_TOKEN'],
    )
    configuration.debug = True  # FIXME comment/uncomment to debug API call logging, do not use in production code base

    with ApiClient(configuration=configuration) as api_client:
        # Create an instance of the API class
        api_instance = ProjectAnalysisApi(api_client)

        # Create and start an analysis for a Nextflow pipeline.
        api_response: AnalysisV4 = api_instance.create_nextflow_analysis(
            project_id,
            nextflow_analysis
        )

        print("-" * 128)
        print(api_response.to_dict())


def create_nextflow_analysis_with_v4():
    configuration = Configuration(
        host=environ['ICAV2_BASE_URL'],
        access_token=environ['ICAV2_ACCESS_TOKEN'],
    )
    configuration.debug = True  # FIXME comment/uncomment to debug API call logging, do not use in production code base

    with ApiClient(configuration=configuration) as api_client:
        api_client.set_default_header(
            header_name="Content-Type",
            header_value="application/vnd.illumina.v4+json",
        )
        api_client.set_default_header(
            header_name="Accept",
            header_value="application/vnd.illumina.v4+json",
        )

        # Create an instance of the API class
        api_instance = ProjectAnalysisApi(api_client)

        # override endpoint settings response type to the version we want i.e. AnalysisV4
        endpoint_settings = api_instance.create_nextflow_analysis_endpoint.settings
        endpoint_settings['response_type'] = (AnalysisV4,)

        # Create and start an analysis for a Nextflow pipeline.
        api_response: AnalysisV4 = api_instance.create_nextflow_analysis(
            project_id,
            nextflow_analysis
        )

        print("-" * 128)
        print(api_response.to_dict())


def create_nextflow_analysis_with_v3():
    configuration = Configuration(
        host=environ['ICAV2_BASE_URL'],
        access_token=environ['ICAV2_ACCESS_TOKEN']
    )
    configuration.debug = True  # FIXME comment/uncomment to debug API call logging, do not use in production code base

    with ApiClient(configuration) as api_client:
        api_client.set_default_header(
            header_name="Content-Type",
            header_value="application/vnd.illumina.v3+json",
        )
        api_client.set_default_header(
            header_name="Accept",
            header_value="application/vnd.illumina.v3+json",
        )

        # Create an instance of the API class
        api_instance = ProjectAnalysisApi(api_client)

        # override endpoint settings response type to the version we want i.e. AnalysisV3 or Analysis
        endpoint_settings = api_instance.create_nextflow_analysis_endpoint.settings
        endpoint_settings['response_type'] = (AnalysisV3,)

        # Create and start an analysis for a Nextflow pipeline.
        api_response: AnalysisV3 = api_instance.create_nextflow_analysis(
            project_id,
            nextflow_analysis,
        )

        print("-" * 128)
        print(api_response.to_dict())


if __name__ == '__main__':
    print(f"libica-{version('libica')}")
    print("-" * 64)

    # See https://github.com/umccr-illumina/libica/issues/135
    # Usage:
    #   cd examples
    #   python issue_135.py 2>&1 | tee issue_135.v3.1.log
    #   python issue_135.py 2>&1 | tee issue_135.v4.1.log
    #   python issue_135.py 2>&1 | tee issue_135.v4.2.log

    # Comment / Uncomment to switch the test cases
    create_nextflow_analysis_with_v3()
    # create_nextflow_analysis_with_v4()
    # create_nextflow_analysis()
