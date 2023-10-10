import os
from contextlib import closing
from unittest import TestCase

from mockito import mock

from libica.openapi.v2 import Configuration, ApiClient
from tests import MOCK_EP


class Issue74IntegrationTests(TestCase):
    """
    dedicated test cases for request in https://github.com/umccr-illumina/libica/issues/74
    the modification patch made is with this PR https://github.com/umccr-illumina/libica/pull/90
    """

    def setUp(self) -> None:
        super(Issue74IntegrationTests, self).setUp()

        icav2_access_token = "MOCK"
        ica_url = MOCK_EP

        self.configuration = Configuration(
            host=ica_url,
            access_token=icav2_access_token,
        )

        with closing(ApiClient(self.configuration)) as _c:
            self.api_client: ApiClient = _c

    def tearDown(self) -> None:
        self.api_client.pool.close()

    def test_configuration_has_custom_attribute(self):
        """
        python -m unittest tests.v2.test_issue_74.Issue74IntegrationTests.test_configuration_has_custom_attribute
        """
        self.assertTrue(hasattr(self.configuration, "form_filename_basename"))

    def test_api_client_must_handle_custom_attribute(self):
        """
        python -m unittest tests.v2.test_issue_74.Issue74IntegrationTests.test_api_client_must_handle_custom_attribute
        """

        self.configuration.form_filename_basename = False
        self.assertFalse(self.api_client.configuration.form_filename_basename)

        mock_file = mock()
        mock_file.name = "some/relative/path/workflow.cwl"
        mock_param_files = {
            "workflowCwlFile": [mock_file]
        }

        params = self.api_client.files_parameters(mock_param_files)
        print(params)

        self.assertEqual(params[0][0], "workflowCwlFile")
        self.assertEqual(params[0][1][0], mock_file.name)

    def test_api_client_must_handle_custom_attribute_true(self):
        """
        python -m unittest tests.v2.test_issue_74.Issue74IntegrationTests.test_api_client_must_handle_custom_attribute_true
        """

        self.configuration.form_filename_basename = True
        self.assertTrue(self.api_client.configuration.form_filename_basename)

        mock_file = mock()
        mock_file.name = "some/relative/path/workflow.cwl"
        mock_param_files = {
            "workflowCwlFile": [mock_file]
        }

        params = self.api_client.files_parameters(mock_param_files)
        print(params)

        self.assertEqual(params[0][0], "workflowCwlFile")
        self.assertEqual(params[0][1][0], os.path.basename(mock_file.name))
