import json
from unittest import skip

from libica.app import wes
from libica.openapi import libwes
from tests.app import IcaUnitTests, IcaIntegrationTests, logger


class WesUnitTests(IcaUnitTests):

    def test_get_run(self):
        """
        python -m unittest tests.app.test_wes.WesUnitTests.test_get_run
        """
        result = wes.get_run("wfr.13245678903214565")
        self.assertTrue(isinstance(result, libwes.WorkflowRun))
        self.assertIsNotNone(result)
        logger.info(f"EXAMPLE MOCK WorkflowRun: \n{result}")

    def test_get_run_to_dict(self):
        """
        python -m unittest tests.app.test_wes.WesUnitTests.test_get_run_to_dict
        """
        result = wes.get_run("wfr.13245678903214565", to_dict=True)
        self.assertTrue(isinstance(result, dict))
        self.assertIsNotNone(result)
        logger.info(f"EXAMPLE MOCK WorkflowRun to_dict(): \n{result}")

    def test_get_run_to_json(self):
        """
        python -m unittest tests.app.test_wes.WesUnitTests.test_get_run_to_json
        """
        result = wes.get_run("wfr.13245678903214565", to_json=True)
        self.assertTrue(isinstance(result, str))
        self.assertIsNotNone(result)
        logger.info(f"EXAMPLE MOCK WorkflowRun to_json(): \n{result}")


class WesIntegrationTests(IcaIntegrationTests):
    # integration test hit actual File or API endpoint, thus, manual run in most cases
    # required appropriate access mechanism setup such as active aws login session
    #
    # export ICA_ACCESS_TOKEN=<ica_v1_development_project_context_jwt_token>
    # uncomment @skip and hit each test case!
    # and keep decorated @skip after tested

    @skip
    def test_get_run(self):
        """
        python -m unittest tests.app.test_wes.WesIntegrationTests.test_get_run
        """
        wfr_id = "wfr.81cf25d7226a4874be43e4b15c1f5687"  # in ICA v1, project context: development
        result = wes.get_run(wfr_id, to_dict=True)
        self.assertEqual(result['id'], wfr_id)
        self.assertIsNotNone(result['input'])
        self.assertIsNotNone(result['output'])

        logger.info("\n" + json.dumps(result['input']))
