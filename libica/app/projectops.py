from contextlib import closing
from typing import List

from libica.app import AppOps
from libica.openapi.v2 import ApiClient
from libica.openapi.v2.api.project_api import ProjectApi
from libica.openapi.v2.model.project import Project
from libica.openapi.v2.model.project_paged_list import ProjectPagedList


class ProjectOps(AppOps):

    def __init__(self, api_client: ApiClient = None):
        super(ProjectOps, self).__init__(api_client=api_client)

    def get_project_list(self) -> List[Project]:
        with closing(self.api_client) as ctx_api_client:
            project_api: ProjectApi = ProjectApi(api_client=ctx_api_client)
            project_list: ProjectPagedList = project_api.get_projects()
            return project_list.items

    def get_project_by_name(self, project_name) -> Project:
        for project in self.get_project_list():
            if project.name == project_name:
                return project

    def get_project_by_id(self, project_id) -> Project:
        with closing(self.api_client) as ctx_api_client:
            project_api: ProjectApi = ProjectApi(api_client=ctx_api_client)
            return project_api.get_project(project_id=project_id)
