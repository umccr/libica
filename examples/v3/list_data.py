"""
Usage:
    Set
        export ICAV2_ACCESS_TOKEN=...
        export ICAV2_PROJECT_ID=...
    Then
        python list_data.py
"""
import os
from importlib.metadata import version

from libica.openapi.v3 import Configuration, ApiClient, ApiException, ProjectDataApi, ProjectDataPagedList, ProjectData

if __name__ == '__main__':
    print(f"libica-{version('libica')}")
    print("-" * 64)

    project_id = os.environ['ICAV2_PROJECT_ID']
    file_path = ["/logs/"]  # empty will list everything under project

    icav2_access_token = os.environ['ICAV2_ACCESS_TOKEN']
    ica_url = "https://ica.illumina.com/ica/rest"

    configuration = Configuration(
        host=ica_url,
        access_token=icav2_access_token,
    )
    # configuration.debug = True  # uncomment to debug API call logging

    api_client = ApiClient(configuration=configuration)

    project_data_api: ProjectDataApi = ProjectDataApi(api_client=api_client)

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
