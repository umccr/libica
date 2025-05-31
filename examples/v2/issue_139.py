from importlib.metadata import version
from os import environ

from libica.openapi.v2 import ApiClient, Configuration, ApiException
from libica.openapi.v2.api.project_pipeline_api import ProjectPipelineApi


def get_icav2_configuration():
    configuration = Configuration(
        host=environ['ICAV2_BASE_URL'],
        access_token=environ['ICAV2_ACCESS_TOKEN']
    )

    configuration.debug = False  # FIXME debug API call logging, do not use in production code base

    return configuration


def get_icav2_client_with(ep_version: int):
    # Create API client
    api_client = ApiClient(get_icav2_configuration())

    # Set endpoint version
    endpoint_version_header = "application/vnd.illumina.v3+json"
    if ep_version == 4:
        endpoint_version_header = "application/vnd.illumina.v4+json"

    api_client.set_default_header(
        header_name="Accept",
        header_value=endpoint_version_header
    )

    return api_client


def get_icav2_client():
    # Create API client
    api_client = ApiClient(get_icav2_configuration())

    # Using `api_client` this way will get response 400 Bad Request like below.
    #
    # At the time writing of this example,
    # The API server enforces that the client must provide the API (media content-type) version.
    # The API server does not automatically fall back (default to) "application/vnd.illumina.v3+json" for the client.
    # FIXME Should this fall back to API default version be server responsibility? Or the client?

    # 400 Bad Request
    # HTTP response body:
    # {
    #     "id": "<1>",
    #     "type": "about:blank",
    #     "title": "ICA_API_004",
    #     "status": 400,
    #     "detail": "Invalid Accept Header",
    #     "instance": "http://ica.illumina.com/ica/rest/api/projects/1/pipelines/2",
    #     "parameters": {},
    #     "timestamp": "2024-08-23T02:33:25Z",
    #     "method": "POST"
    # }

    return api_client


if __name__ == '__main__':
    print(f"libica-{version('libica')}")
    print("-" * 64)

    # See https://github.com/umccr/libica/issues/139
    # Usage:
    #   export ICAV2_BASE_URL=https://ica.illumina.com/ica/rest
    #   export ICAV2_ACCESS_TOKEN=<token>
    #   pip install libica
    #   python issue_139.py

    # Change these variable to suit your situation
    project_id = "ea19a3f5-ec7c-4940-a474-c31cd91dbad4"
    pipeline_id = "2cd57144-d568-4f0b-b85e-734d82e654b9"

    # FIXME In v3 SDK, this now set to application/vnd.illumina.v3+json by default
    client = get_icav2_client()

    # Client must explicitly set the version.
    # client = get_icav2_client_with(ep_version=3)
    # client = get_icav2_client_with(ep_version=4)

    # Or, you can override to Accept all media types.
    # See https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Accept
    #
    # This is the setting needed in content downloading. See issue_137.py
    # client.set_default_header(
    #     header_name="Accept",
    #     header_value="*/*"
    # )

    project_pipeline_api = ProjectPipelineApi(api_client=client)

    try:

        # NOTE:
        # You can try link / unlink, alternatively.
        # If the pipeline is already linked to the project, you get "404 Not Found" response
        # with message  "[...] is not eligible to be added to the project"

        resp = project_pipeline_api.link_pipeline_to_project(project_id=project_id, pipeline_id=pipeline_id)
        # resp = project_pipeline_api.unlink_pipeline_from_project(project_id=project_id, pipeline_id=pipeline_id)

        assert resp is None  # If operation is successful, response should be None

    except ApiException as e:
        print("Exception when calling ProjectPipelineApi->link_pipeline_to_project: %s\n" % e)
