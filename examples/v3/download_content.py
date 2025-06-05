import os
import re
import tempfile
from importlib.metadata import version
from os import environ
from pathlib import Path

from libica.openapi.v3 import Configuration, ApiClient, ApiException, PipelineApi
from libica.openapi.v3.rest import RESTResponseType

if __name__ == '__main__':

    print(f"libica-{version('libica')}")
    print("-" * 64)

    # See https://github.com/umccr/libica/issues/137

    # curl -s -H "Authorization: Bearer $ICAV2_ACCESS_TOKEN" "https://ica.illumina.com/ica/rest/api/pipelines/2cd57144-d568-4f0b-b85e-734d82e654b9/files" | jq
    # curl -vvv -s -H "Authorization: Bearer $ICAV2_ACCESS_TOKEN" "https://ica.illumina.com/ica/rest/api/pipelines/2cd57144-d568-4f0b-b85e-734d82e654b9/files/16498d5f-bebd-4d70-95eb-6c381d41712b/content"

    # Usage:
    #   icav2 tenants enter umccr-prod
    #   icav2 projects enter 'development'
    #   icav2 pipelines get 2cd57144-d568-4f0b-b85e-734d82e654b9
    #   python issue_137.py

    pipeline_id = "2cd57144-d568-4f0b-b85e-734d82e654b9"
    # file_id = "b59f0a4b-2370-40d8-94ea-25c6c5c0f710" # works fine
    file_id = "16498d5f-bebd-4d70-95eb-6c381d41712b"

    configuration = Configuration(
        host=environ['ICAV2_BASE_URL'],
        access_token=environ['ICAV2_ACCESS_TOKEN']
    )

    # configuration.debug = True  # FIXME debug API call logging, do not use in production code base

    with ApiClient(configuration) as api_client:
        # Set Accept header to * or application/octet-stream
        api_client.set_default_header(
            header_name="Accept",
            # header_value="*/*",
            header_value="application/octet-stream",
        )

        api_instance = PipelineApi(api_client)
        try:
            # Download the contents of a pipeline file.
            # Use without a preload content method instead of `download_pipeline_file_content(...)`
            api_response: RESTResponseType = api_instance.download_pipeline_file_content_without_preload_content(
                pipeline_id=pipeline_id,
                file_id=file_id,
            )

            # we are going to deserialize ourselves for the filename with mid-path(s), if any

            print(type(api_response))  # raw `urllib3.response.HTTPResponse`

            response_data = api_response.data  # get the data content
            content_disposition = api_response.headers.get("Content-Disposition")  # get header content disposition

            filename = re.search(r'filename=[\'"]?([^\'"\s]+)[\'"]?', content_disposition).group(1)
            print(filename)

            with tempfile.TemporaryDirectory(delete=False) as td:  # setting `delete=True` will remove once out of scope
                path = os.path.join(td, filename)  # full path
                Path(path).parent.mkdir(parents=True, exist_ok=True)  # same as `mkdir -p <parent-mid-dirs>`
                with open(path, 'wb') as fh:
                    if isinstance(response_data, str):
                        # change str to bytes so we can write it
                        response_data = response_data.encode('utf-8')
                    fh.write(response_data)

            print(fh.name)

        except ApiException as e:
            print("Exception when calling PipelineApi->download_pipeline_file_content: %s\n" % e)
            raise ApiException
