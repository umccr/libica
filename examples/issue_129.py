# Standard imports
from os import environ

from libica.openapi.v2 import ApiClient, ApiException
# Local imports
from libica.openapi.v2 import Configuration
from libica.openapi.v2.api.project_pipeline_api import ProjectPipelineApi
from libica.openapi.v2.model.pipeline_configuration_parameter_list import PipelineConfigurationParameterList

# Set configuration
icav2_configuration = Configuration(
    host=environ['ICAV2_BASE_URL'],
    access_token=environ['ICAV2_ACCESS_TOKEN']
)

# Set variables
pipeline_id = "fdef5902-3f50-4ee7-ae17-15d38d4b489c"
project_id = "7595e8f2-32d3-4c76-a324-c6a85dae87b5"

if __name__ == '__main__':
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

# See https://github.com/umccr-illumina/libica/issues/129
