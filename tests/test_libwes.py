from contextlib import closing
from unittest import TestCase

from libica.openapi import libwes
from libica.openapi.libwes import WorkflowList, WorkflowCompact, Workflow, WorkflowVersion, \
    UpdateWorkflowVersionRequest, WorkflowLanguage
from . import _logger, MOCK_EP


class LibWESIntegrationTests(TestCase):

    def setUp(self) -> None:
        super(LibWESIntegrationTests, self).setUp()

        ica_access_token = "MOCK"
        ica_base_url = MOCK_EP

        self.configuration = libwes.Configuration(
            host=ica_base_url,
            api_key={
                'Authorization': ica_access_token
            },
            api_key_prefix={
                'Authorization': "Bearer"
            },
        )

        with closing(libwes.ApiClient(self.configuration)) as _c:
            self.api_client = _c

    def tearDown(self) -> None:
        self.api_client.pool.close()

    def test_get_workflow(self):
        wfl_api: libwes.WorkflowsApi = libwes.WorkflowsApi(self.api_client)
        wfl_id = "mock"
        wfl: Workflow = wfl_api.get_workflow(workflow_id=wfl_id)
        self.assertIsNotNone(wfl)
        _logger.info(wfl.name)

    def test_list_workflows(self):
        wfl_api: libwes.WorkflowsApi = libwes.WorkflowsApi(self.api_client)
        try:
            page_token = None
            while True:
                wfl_list: WorkflowList = wfl_api.list_workflows(page_size=1000, page_token=page_token)
                self.assertIsNotNone(wfl_list.items)
                # _logger.info(wfl_list)
                for item in wfl_list.items:
                    wfl: WorkflowCompact = item
                    # _logger.info(wfl.id)
                    _logger.info(wfl.name)
                page_token = wfl_list.next_page_token
                if not wfl_list.next_page_token:
                    break
        except libwes.ApiException as e:
            _logger.error(e)

    def test_get_workflow_version(self):
        """
        python -m unittest tests.integration.test_libwes.LibWESIntegrationTests.test_get_workflow_version
        """
        wfv_api: libwes.WorkflowVersionsApi = libwes.WorkflowVersionsApi(self.api_client)
        wfv: WorkflowVersion = wfv_api.get_workflow_version(workflow_id="wfl.id_does_matter", version_name="v1")
        self.assertIsNotNone(wfv)
        _logger.info(wfv)

    def test_update_workflow_version(self):
        """
        python -m unittest tests.integration.test_libwes.LibWESIntegrationTests.test_update_workflow_version
        """
        wfv_api: libwes.WorkflowVersionsApi = libwes.WorkflowVersionsApi(self.api_client)

        current_wfv: WorkflowVersion = wfv_api.get_workflow_version(workflow_id="wfl.id", version_name="current_ver")
        desc = current_wfv.definition
        _logger.info(desc)

        body: UpdateWorkflowVersionRequest = UpdateWorkflowVersionRequest(
            version="0.2-redirect-nolisting",
            description="Uses sambamda slice and samtools to extract hla contigs, chr6 hla region and unmapped bams. "
                        "Align all to razers3 and then place through optitype workflow",
            language=WorkflowLanguage(name="CWL", version="1.1"),
            definition={'$graph': [{'class': "..."}]}
        )

        wfv: WorkflowVersion = wfv_api.update_workflow_version(
            workflow_id="wfl.id_does_matter", version_name="0.2-redirect-nolisting", body=body
        )

        self.assertIsNotNone(wfv)
        _logger.info(wfv)
