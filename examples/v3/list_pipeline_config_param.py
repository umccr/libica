from os import environ

from libica.openapi.v3 import Configuration, ApiClient, ProjectPipelineApi, PipelineConfigurationParameterList, \
    ApiException

# Set configuration
icav2_configuration = Configuration(
    host=environ['ICAV2_BASE_URL'],
    access_token=environ['ICAV2_ACCESS_TOKEN']
)

# Set variables
pipeline_ids = [
    "a0778b16-f318-40df-ae04-95998e3a7564",
    "c2dfdbaa-2074-44c7-8078-d33e13607061",
    "cb4bf1cf-b796-488c-8d88-e75fcb9336e1",
    "35cae57c-8895-4814-ae89-db4b5e9668b2",
    "fcc6d555-4ea3-414e-8264-3bf362d81c58",
    "71f094dc-0cf8-4fcf-890c-9f3edf00ee20",
    "fe6df931-4a30-4fa7-8d05-31e00367d216",
    "fb8ba85b-244f-47c1-82cb-baea6db9d90d",
    "d1e84505-3082-4e0b-b246-cc952c8b1b73",
    "bd6e5690-3ccf-4ac4-997d-59462f852f65",
    "e51d4372-4567-4ff8-ac72-f7d754a75af7",
]
project_id = "ea19a3f5-ec7c-4940-a474-c31cd91dbad4"

if __name__ == '__main__':

    # See https://github.com/umccr/libica/issues/129
    #
    # curl -s -H "Authorization: Bearer $ICAV2_ACCESS_TOKEN" "https://ica.illumina.com/ica/rest/api/projects/ea19a3f5-ec7c-4940-a474-c31cd91dbad4/pipelines/a0778b16-f318-40df-ae04-95998e3a7564/configurationParameters" | jq
    #
    # Usage:
    #   icav2 tenants enter umccr-prod
    #   icav2 projects enter 'development'
    #   python list_pipeline_config_param.py

    for pipeline_id in pipeline_ids:

        # Enter a context with an instance of the API client
        with ApiClient(icav2_configuration) as api_client:
            # Create an instance of the API class
            api_instance = ProjectPipelineApi(api_client)

            try:
                # Retrieve input parameters for a project pipeline.
                api_response: PipelineConfigurationParameterList = api_instance.get_project_pipeline_configuration_parameters(
                    project_id, pipeline_id
                )
            except ApiException as e:
                raise ApiException(
                    "Exception when calling ProjectPipelineApi->get_project_pipeline_input_parameters: %s\n" % e)

        print(api_response.items)
