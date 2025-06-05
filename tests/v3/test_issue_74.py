import os
from unittest import TestCase

from mockito import mock

from libica.openapi.v3 import Configuration, ApiClient
from tests import MOCK_EP


class Issue74IntegrationTests(TestCase):
    """
    dedicated test cases for request in https://github.com/umccr/libica/issues/74
    the modification patch made in v2 SDK with this PR https://github.com/umccr/libica/pull/90
    """

    def setUp(self) -> None:
        super(Issue74IntegrationTests, self).setUp()

        icav2_access_token = "MOCK"
        ica_url = MOCK_EP

        self.configuration = Configuration(
            host=ica_url,
            access_token=icav2_access_token,
        )

        self.api_client: ApiClient = ApiClient(self.configuration)

    def tearDown(self) -> None:
        super(Issue74IntegrationTests, self).tearDown()

    def test_configuration_no_custom_attribute(self):
        """
        python -m unittest tests.v3.test_issue_74.Issue74IntegrationTests.test_configuration_no_custom_attribute
        """
        self.assertFalse(hasattr(self.configuration, "form_filename_basename"))

    def test_api_client_must_handle_file_hierarchy(self):
        """
        python -m unittest tests.v3.test_issue_74.Issue74IntegrationTests.test_api_client_must_handle_file_hierarchy

        In SDK v3, ApiClient comes built-in handling of this, which might simplify the implementation.
        To mimic v2 SDK behaviour with the File instance, try as follows.
        """

        self.configuration.form_filename_basename = False
        self.assertFalse(self.api_client.configuration.form_filename_basename)

        # Simulate read the File bytes before passing on to ApiClient for the POST request
        mock_file = mock(bytes)
        mock_file.name = "some/relative/path/workflow.cwl"

        mock_param_files = {
            "workflowCwlFile": (mock_file.name, mock_file)  # tuple("structure/to/keep/hello.cwl", bytes<FileContent>)
        }

        # Now simulate calling ApiClient POST request
        params = self.api_client.files_parameters(mock_param_files)
        print(params)

        self.assertEqual(params[0][0], "workflowCwlFile")
        self.assertEqual(params[0][1][0], mock_file.name)

    def test_api_client_must_handle_file_hierarchy_2(self):
        """
        python -m unittest tests.v3.test_issue_74.Issue74IntegrationTests.test_api_client_must_handle_file_hierarchy_2
        """

        mock_file = mock(bytes)
        mock_file.name = "some/relative/path/workflow.cwl"

        mock_param_files = {
            mock_file.name: mock_file
        }

        params = self.api_client.files_parameters(mock_param_files)
        print(params)

        self.assertEqual(params[0][0], mock_file.name)
        self.assertEqual(params[0][1][0], "some/relative/path/workflow.cwl")

    def test_api_client_must_handle_file_hierarchy_3(self):
        """
        python -m unittest tests.v3.test_issue_74.Issue74IntegrationTests.test_api_client_must_handle_file_hierarchy_3
        """

        current_dir = os.path.dirname(__file__)
        file_path_on_local = os.path.join(current_dir, "hello", "workflow.cwl")

        virtual_path_on_remote = "some/relative/path/workflow.cwl"

        mock_param_files = {
            virtual_path_on_remote: file_path_on_local
        }

        params = self.api_client.files_parameters(mock_param_files)
        print(params)

        self.assertEqual(params[0][0], virtual_path_on_remote)
        self.assertEqual(params[0][1][0], os.path.basename(file_path_on_local))
