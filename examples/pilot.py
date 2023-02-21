"""
Usage:
    Set
        export ICAV2_ACCESS_TOKEN=...
        export ICA_PROJECT=...
    Then
        python pilot.py
"""
import os
from contextlib import closing

from libica.openapi.v2 import Configuration, ApiClient, ApiException
from libica.openapi.v2.api.project_data_api import ProjectDataApi
from libica.openapi.v2.model.project_data import ProjectData
from libica.openapi.v2.model.project_data_paged_list import ProjectDataPagedList

if __name__ == '__main__':

    project_id = os.environ['ICA_PROJECT']
    file_path = ["/test_folder/"]  # empty will list everything under project

    icav2_access_token = os.environ['ICAV2_ACCESS_TOKEN']
    ica_url = "https://ica.illumina.com/ica/rest"

    configuration = Configuration(
        host=ica_url,
        access_token=icav2_access_token,
    )
    # configuration.debug = True  # uncomment to debug API call logging

    api_client = ApiClient(
        configuration=configuration,
        header_name="Content-Type",
        header_value="application/vnd.illumina.v3+json",
    )

    with closing(api_client) as ctx_api_client:
        project_data_api: ProjectDataApi = ProjectDataApi(api_client=ctx_api_client)

        try:
            page_token = ""
            while True:
                project_data_paged_list: ProjectDataPagedList = project_data_api.get_project_data_list(
                    project_id=project_id,
                    file_path=file_path,
                    page_size=str(1000),
                    page_token=page_token,
                )

                for item in project_data_paged_list.items:
                    project_data: ProjectData = item
                    print((
                        project_data.data.id,  # fil.<ID> (or) fol.<ID>
                        project_data.data.details.path,
                        project_data.data.details.data_type,
                    ))

                page_token = project_data_paged_list.next_page_token
                if not project_data_paged_list.next_page_token:
                    break

        except ApiException as e:
            print(e)
