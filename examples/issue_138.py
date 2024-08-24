from os import environ

from importlib.metadata import version

from libica.openapi.v2 import ApiClient, Configuration, ApiException
from libica.openapi.v2.api.project_pipeline_api import ProjectPipelineApi
from libica.openapi.v2.model.pipeline_configuration_parameter_list import PipelineConfigurationParameterList

if __name__ == '__main__':

    print(f"libica-{version('libica')}")
    print("-" * 64)

    # See https://github.com/umccr-illumina/libica/issues/138
    # Usage:
    #   icav2 tenants enter umccr-beta
    #   icav2 projects enter 'ega-upload-test'
    #   python issue_138.py

    project_id = 'd3697f78-22b0-41e2-96f6-d105715239f3'
    pipeline_id = '024dd8d0-6ff5-4641-a6e6-cc5c7d30e2e7'

    configuration = Configuration(
        host=environ['ICAV2_BASE_URL'],
        access_token=environ['ICAV2_ACCESS_TOKEN']
    )

    configuration.debug = False  # FIXME debug API call logging, do not use in production code base

    with ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = ProjectPipelineApi(api_client)

        try:
            # Retrieve input parameters for a project pipeline.
            api_response: PipelineConfigurationParameterList = api_instance.get_project_pipeline_configuration_parameters(
                project_id=project_id,
                pipeline_id=pipeline_id,
                _check_return_type=False,  # FIXME force type checking off for the data received from the server
            )

            print(api_response)

            print("-" * 64)

            print(api_response.items[22])  # FIXME offending type conversion value

            assert type(api_response.items[22]['settings']['defaultValues'][0]), int

            # TRACE:
            # model_utils.py > validate_and_convert_types > attempt_convert_item
            # libica.openapi.v2.exceptions.ApiTypeError: Invalid type for variable '0'. Required value type is str and
            # passed type was int at ['received_data']['items'][22]['settings']['default_values'][0]

        except ApiException as e:
            print("Exception when calling ProjectPipelineApi->get_project_pipeline_configuration_parameters: %s\n" % e)
            raise ApiException
