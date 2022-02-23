import uuid
from contextlib import closing
from unittest import TestCase

from libica.openapi.v2 import Configuration, ApiClient, ApiException
from libica.openapi.v2.api.project_api import ProjectApi
from libica.openapi.v2.api.project_data_api import ProjectDataApi
from libica.openapi.v2.model.create_project import CreateProject
from libica.openapi.v2.model.project import Project
from libica.openapi.v2.model.project_data import ProjectData
from libica.openapi.v2.model.project_data_paged_list import ProjectDataPagedList
from libica.openapi.v2.model.project_paged_list import ProjectPagedList
from libica.openapi.v2.model.project_tag import ProjectTag
from . import _logger, MOCK_EP


class ProjectIntegrationTests(TestCase):

    def setUp(self) -> None:
        super(ProjectIntegrationTests, self).setUp()

        icav2_access_token = "MOCK"
        ica_url = MOCK_EP

        self.configuration = Configuration(
            host=ica_url,
            access_token=icav2_access_token,
        )

        with closing(ApiClient(self.configuration)) as _c:
            self.api_client = _c

    def tearDown(self) -> None:
        self.api_client.pool.close()

    def test_get_project(self):
        """
        python -m unittest tests.test_project.ProjectIntegrationTests.test_get_project
        """
        project_api: ProjectApi = ProjectApi(api_client=self.api_client)
        project_id = "mock"
        project: Project = project_api.get_project(project_id=project_id)
        self.assertIsNotNone(project)
        _logger.info((project.id, project.name))

    def test_get_projects(self):
        """
        python -m unittest tests.test_project.ProjectIntegrationTests.test_get_projects
        """
        project_api: ProjectApi = ProjectApi(api_client=self.api_client)
        try:
            page_token = ""
            while True:
                project_paged_list: ProjectPagedList = project_api.get_projects(
                    page_size=str(1000),
                    page_token=page_token,
                )
                self.assertIsNotNone(project_paged_list.items)
                # _logger.info(project_paged_list)
                for item in project_paged_list.items:
                    project: Project = item
                    _logger.info((project.id, project.name))
                page_token = project_paged_list.next_page_token
                if not project_paged_list.next_page_token:
                    break
        except ApiException as e:
            _logger.error(e)

    def test_create_project(self):
        """
        python -m unittest tests.test_project.ProjectIntegrationTests.test_create_project
        """
        project_api: ProjectApi = ProjectApi(api_client=self.api_client)
        create_project = CreateProject(
            name="AH",
            short_description="short_description_example",
            information="information_example",
            project_owner_id=str(uuid.uuid4()),
            region_id=str(uuid.uuid4()),
            billing_mode="PROJECT",
            data_sharing_enabled=True,
            tags=ProjectTag(
                technical_tags=[
                    "technical_tags_example",
                ],
                user_tags=[
                    "user_tags_example",
                ],
            ),
            storage_bundle_id=str(uuid.uuid4()),
            metadata_model_id=str(uuid.uuid4()),
            storage_configuration_id=str(uuid.uuid4()),
            storage_configuration_subfolder="storage_configuration_subfolder_example",
        )
        try:
            project: Project = project_api.create_project(create_project=create_project)
            self.assertIsNotNone(project)
            _logger.info(project)
        except ApiException as e:
            _logger.error("Exception when calling ProjectApi->create_project: %s\n" % e)

    def test_get_project_data_list(self):
        """
        python -m unittest tests.test_project.ProjectIntegrationTests.test_get_project_data_list
        """
        project_data_api: ProjectDataApi = ProjectDataApi(api_client=self.api_client)
        mock_project_id = str(uuid.uuid4())
        try:
            page_token = ""
            while True:
                project_data_paged_list: ProjectDataPagedList = project_data_api.get_project_data_list(
                    project_id=mock_project_id,
                    page_size=str(1000),
                    page_token=page_token,
                )
                self.assertIsNotNone(project_data_paged_list.items)
                # _logger.info(project_data_paged_list)
                for item in project_data_paged_list.items:
                    project_data: ProjectData = item
                    if project_data.data.details is not None:
                        _logger.info((
                            project_data.data.details.name,
                            project_data.data.details.path,
                            project_data.data.details.data_type,
                            project_data.data.details.status,
                            project_data.data.details.file_size_in_bytes,
                            project_data.data.details.time_created,
                        ))
                    else:
                        _logger.info(f"[SKIP] project_data.data.details is {project_data.data}")
                page_token = project_data_paged_list.next_page_token
                if not project_data_paged_list.next_page_token:
                    break
        except ApiException as e:
            _logger.error(e)
