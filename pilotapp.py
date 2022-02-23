"""
Usage:
    Either
        Have your `icav2` CLI setup and able to do `icav2 projects enter playground_v2 && icav2 projectdata list`
    Or
        export ICAV2_ACCESS_TOKEN=...
        export ICA_PROJECT=...
    Then
        python pilotapp.py
"""
from contextlib import closing

from libica.app import AppHelper, ProjectDataType
from libica.app.dataops import ProjectDataOps
from libica.openapi.v2 import ApiClient
from libica.openapi.v2.model.project_data import ProjectData


def list_all_files():
    selected = None  # we will browse through project data and will pick the first file found

    for item in dataops.list_files():
        project_data: ProjectData = item
        if project_data.data.details is not None:
            print((
                project_data.data.id,  # fil.<ID> (or) fol.<ID>
                project_data.data.details.path,
                project_data.data.details.data_type,
                # project_data.data.details.name,
                # project_data.data.details.status,
                # project_data.data.details.file_size_in_bytes,
                # project_data.data.details.time_created,
            ))

            if not selected and project_data.data.details.data_type == ProjectDataType.FILE.value:
                selected = project_data.data.details.path
        else:
            print(f"[SKIP] project_data.data.details is {project_data.data}")

    return selected


def download_and_read_lines(file_path):
    print(f"Downloading {file_path} from project_id {project_id}")
    print()
    ntf = dataops.download_file(file_path=file_path)
    with closing(ntf) as cf:
        with open(cf.name, 'r') as f:
            for line in f.readlines():
                print(line)


if __name__ == '__main__':

    app_helper = AppHelper(debug=False)
    project_id = app_helper.get_icav2_cli_session_project_id()

    cli_session_api_client: ApiClient = app_helper \
        .build_icav2_configuration_with_cli_session() \
        .get_icav2_api_client()

    dataops = ProjectDataOps(project_id=project_id, api_client=cli_session_api_client)

    selected_file_path = list_all_files()

    print('-' * 64)

    if selected_file_path:
        download_and_read_lines(selected_file_path)
    else:
        print(f"No file found in project_id {project_id}")
