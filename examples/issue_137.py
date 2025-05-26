import os
import re
import tempfile
from importlib.metadata import version
from os import environ
from pathlib import Path

from urllib3 import HTTPResponse

from libica.openapi.v2 import ApiClient, Configuration, ApiException
from libica.openapi.v2.api.pipeline_api import PipelineApi

if __name__ == '__main__':

    print(f"libica-{version('libica')}")
    print("-" * 64)

    # See https://github.com/umccr/libica/issues/137

    # curl -s -H "Authorization: Bearer $ICAV2_ACCESS_TOKEN" "https://ica.illumina.com/ica/rest/api/pipelines/a10cad1d-b3c6-4a6e-8f44-0605fbe269d5/files" | jq
    # curl -vvv -s -H "Authorization: Bearer $ICAV2_ACCESS_TOKEN" "https://ica.illumina.com/ica/rest/api/pipelines/a10cad1d-b3c6-4a6e-8f44-0605fbe269d5/files/31a36b7a-f034-4bbc-ba3e-229d6ab866f4/content" | jq

    # Usage:
    #   icav2 tenants enter umccr-beta
    #   icav2 projects enter 'playground_v2'
    #   icav2 pipelines get a10cad1d-b3c6-4a6e-8f44-0605fbe269d5
    #   python issue_137.py

    pipeline_id = "a10cad1d-b3c6-4a6e-8f44-0605fbe269d5"
    # file_id = "0a7b29b7-ae8f-4198-85f3-0743f8290a25"  # works fine
    file_id = "31a36b7a-f034-4bbc-ba3e-229d6ab866f4"

    configuration = Configuration(
        host=environ['ICAV2_BASE_URL'],
        access_token=environ['ICAV2_ACCESS_TOKEN']
    )

    # configuration.debug = True  # FIXME debug API call logging, do not use in production code base

    with ApiClient(configuration) as api_client:
        api_instance = PipelineApi(api_client)
        try:
            # Download the contents of a pipeline file.
            api_response: HTTPResponse = api_instance.download_pipeline_file_content(
                pipeline_id=pipeline_id,
                file_id=file_id,
                _preload_content=False,  # disable built-in deserialize_file method which assume flat file structure
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
