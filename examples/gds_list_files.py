"""
Usage:
        export ICA_ACCESS_TOKEN=...
        export ICA_BASE_URL=...
    Then
        python gds_list_files.py
"""
import os

from libica.openapi import libgds

ica_access_token = os.environ['ICA_ACCESS_TOKEN']
ica_base_url = os.getenv('ICA_BASE_URL', "https://aps2.platform.illumina.com")

# Construct API client config object
gds_configuration = libgds.Configuration(
    host=ica_base_url,
    api_key={
        'Authorization': ica_access_token
    },
    api_key_prefix={
        'Authorization': "Bearer"
    },
)
# Debug print REST call which include token, should be commented in PRODUCTION code
# gds_configuration.debug = True

if __name__ == '__main__':

    with libgds.ApiClient(gds_configuration) as api_client:

        # THIS WON'T WORK
        # volume_name = "umccr-temp-data-dev"
        # output_path = "/*"

        # MUST WRAP IN THE BRACKET
        volume_name = ["development", ]
        output_path = ["/reference-data/genomes/hg38/*", ]

        files_api = libgds.FilesApi(api_client)
        try:
            page_token = None
            while True:
                file_list: libgds.FileListResponse = files_api.list_files(
                    volume_name=volume_name,
                    path=output_path,
                    page_size=1000,
                    page_token=page_token,
                )

                for item in file_list.items:
                    file: libgds.FileResponse = item
                    print(file.name)

                page_token = file_list.next_page_token
                if not file_list.next_page_token:
                    break
            # end while

        except libgds.ApiException as e:
            print(f"Exception when calling list_files: \n{e}")
