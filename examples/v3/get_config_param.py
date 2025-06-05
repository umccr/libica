from importlib.metadata import version
from os import environ

from libica.openapi.v3 import Configuration, ApiClient, ApiException, ProjectPipelineApi, \
    PipelineConfigurationParameterList, PipelineConfigurationParameter

if __name__ == '__main__':

    print(f"libica-{version('libica')}")
    print("-" * 64)

    # See https://github.com/umccr/libica/issues/138
    # Usage:
    #   icav2 tenants enter umccr-prod
    #   icav2 projects enter 'development'
    #   python issue_138.py

    project_id = 'ea19a3f5-ec7c-4940-a474-c31cd91dbad4'
    pipeline_id = '510c7608-62ac-43bd-b114-d28475125118'

    configuration = Configuration(
        host=environ['ICAV2_BASE_URL'],
        access_token=environ['ICAV2_ACCESS_TOKEN']
    )

    # configuration.debug = False  # FIXME debug API call logging, do not use in production code base

    with ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = ProjectPipelineApi(api_client)

        try:
            # Retrieve input parameters for a project pipeline.
            api_response: PipelineConfigurationParameterList = api_instance.get_project_pipeline_configuration_parameters(
                project_id=project_id,
                pipeline_id=pipeline_id,
            )

            print(api_response.to_json())

            print("-" * 64)

            int_param: PipelineConfigurationParameter = api_response.items[19]  # FIXME pick the one with integer type

            assert type(int_param.settings.to_dict()['defaultValues'][0]), int

        except ApiException as e:
            print("Exception when calling ProjectPipelineApi->get_project_pipeline_configuration_parameters: %s\n" % e)
            raise ApiException
