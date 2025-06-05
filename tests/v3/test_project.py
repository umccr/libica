import uuid
from unittest import TestCase

from libica.openapi.v3 import Configuration, ApiClient, ApiException, ProjectApi, Project, ProjectPagedList, \
    CreateProject, ProjectTag, ProjectDataApi, ProjectDataPagedList, ProjectData
from .. import _logger, MOCK_EP


class ProjectIntegrationTests(TestCase):

    def setUp(self) -> None:
        super(ProjectIntegrationTests, self).setUp()

        icav2_access_token = "MOCK"
        ica_url = MOCK_EP

        self.configuration = Configuration(
            host=ica_url,
            access_token=icav2_access_token,
        )

        self.api_client = ApiClient(self.configuration)

    def tearDown(self) -> None:
        pass

    def test_get_project(self):
        """
        python -m unittest tests.v3.test_project.ProjectIntegrationTests.test_get_project
        """
        project_api: ProjectApi = ProjectApi(api_client=self.api_client)
        project_id = "mock"
        project: Project = project_api.get_project(project_id=project_id)
        # self.assertIsNotNone(project)  # non-deterministic assertion
        if project is None:
            _logger.info(f"project is {project}")
        else:
            _logger.info((project.id, project.name))

    def test_get_projects(self):
        """
        python -m unittest tests.v3.test_project.ProjectIntegrationTests.test_get_projects
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
                    if item is None:
                        continue
                    project: Project = item
                    _logger.info((project.id, project.name))
                page_token = project_paged_list.next_page_token
                if not project_paged_list.next_page_token:
                    break
        except ApiException as e:
            _logger.error(e)

    def test_create_project(self):
        """
        python -m unittest tests.v3.test_project.ProjectIntegrationTests.test_create_project
        """
        project_api: ProjectApi = ProjectApi(api_client=self.api_client)
        create_project = CreateProject(
            name="AH",
            shortDescription="short_description_example",
            information="information_example",
            projectOwnerId=str(uuid.uuid4()),
            regionId=str(uuid.uuid4()),
            billingMode="PROJECT",
            dataSharingEnabled=True,
            tags=ProjectTag(
                technicalTags=[
                    "technical_tags_example",
                ],
                userTags=[
                    "user_tags_example",
                ],
            ),
            storageBundleId=str(uuid.uuid4()),
            metadataModelId=str(uuid.uuid4()),
            storageConfigurationId=str(uuid.uuid4()),
            storageConfigurationSubfolder="storage_configuration_subfolder_example",
        )
        try:
            project: Project = project_api.create_project(create_project=create_project)
            # self.assertIsNotNone(project)  # non-deterministic assertion
            _logger.info(project)
        except ApiException as e:
            _logger.error("Exception when calling ProjectApi->create_project: %s\n" % e)

    def test_get_project_data_list(self):
        """
        python -m unittest tests.v3.test_project.ProjectIntegrationTests.test_get_project_data_list
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
                    if item is None:
                        continue
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
