"""
Usage:
    Either
        Have your `icav2` CLI setup and able to do `icav2 projects enter playground_v2 && icav2 projectdata list`
    Or
        export ICAV2_ACCESS_TOKEN=...
        export ICAV2_PROJECT_ID=...
    Then
        python pilotapp.py
"""
from contextlib import closing

from libica.app import AppHelper, ProjectDataType
from libica.app.dataops import ProjectDataOps, ProjectDataOpsFactory
from libica.openapi.v2 import ApiClient
from libica.openapi.v2.model.project_data import ProjectData


def use_case1():

    def list_all_files():
        selected = None  # we will browse through project data and randomly pick the first txt file found and break

        for item in project_dataops.list_files():
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

                if not selected and \
                        project_data.data.details.data_type == ProjectDataType.FILE.value and \
                        str(project_data.data.details.path).endswith('.txt'):
                    selected = project_data.data.details.path
                    break
            else:
                print(f"[SKIP] project_data.data.details is {project_data.data}")

        return selected

    def download_and_read_lines(file_path):
        print(f"Downloading {file_path} from project {project_dataops.project.name}")
        project_dataops.file_path = file_path  # could also do `project_dataops.cd(file_path)`
        ntf = project_dataops.download_file()
        with closing(ntf) as cf:
            with open(cf.name, 'r') as f:
                for line in f.readlines():
                    print(line)

    project_id = app_helper.get_icav2_cli_session_project_id()

    project_dataops = ProjectDataOps(project_id=project_id, api_client=cli_session_api_client)
    project_dataops.cd("/test_folder/")

    selected_file_path = list_all_files()

    print('-' * 64)

    if selected_file_path:
        download_and_read_lines(selected_file_path)
    else:
        print(f"No file found in project {project_dataops.project.name}")


def use_case2():
    """NOTE: this URI scheme use case is still experimental.
    Though the concept is simple such that --

    It mimics the GDS scheme as follows:
        THEN
            gds://volume_name/path/to/folder/file.txt
        NOW
            icav2://owning-project-name/path/to/folder/
            icav2://owning-project-name/path/to/file.txt
    """
    icav2_uri = "icav2://playground_v2/test_folder/foo1.txt"
    prj_dataops: ProjectDataOps = ProjectDataOpsFactory(api_client=cli_session_api_client).from_uri(icav2_uri=icav2_uri)
    print(prj_dataops.create_presigned_url())


if __name__ == '__main__':

    app_helper = AppHelper(debug=False)

    cli_session_api_client: ApiClient = app_helper \
        .build_icav2_configuration_with_cli_session() \
        .get_icav2_api_client()

    use_case1()

    print('-' * 64)

    use_case2()
