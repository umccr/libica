import logging
import os
from contextlib import closing
from unittest import TestCase

from libiap.openapi import libwes
from libiap.openapi.libwes import WorkflowList, WorkflowCompact, Workflow
from tests.integration import WES_MOCK_EP

logger = logging.getLogger(__name__)


class LibWESIntegrationTests(TestCase):

    def setUp(self) -> None:
        super(LibWESIntegrationTests, self).setUp()

        iap_auth_token = os.getenv("IAP_AUTH_TOKEN", None)
        iap_base_url = os.getenv("IAP_BASE_URL", None)

        if iap_base_url is None or iap_auth_token is None:
            iap_auth_token = "MOCK"
            iap_base_url = WES_MOCK_EP

        self.configuration = libwes.Configuration(
            host=iap_base_url,
            api_key={
                'Authorization': iap_auth_token
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
        wfl_id = os.getenv("IAP_WES_WORKFLOW_ID", "mock")
        wfl: Workflow = wfl_api.get_workflow(workflow_id=wfl_id)
        self.assertIsNotNone(wfl)
        logger.info(wfl.name)

    def test_list_workflows(self):
        wfl_api: libwes.WorkflowsApi = libwes.WorkflowsApi(self.api_client)
        try:
            page_token = None
            while True:
                wfl_list: WorkflowList = wfl_api.list_workflows(page_size=1000, page_token=page_token)
                self.assertIsNotNone(wfl_list.items)
                # logger.info(wfl_list)
                for item in wfl_list.items:
                    wfl: WorkflowCompact = item
                    # logger.info(wfl.id)
                    logger.info(wfl.name)
                page_token = wfl_list.next_page_token
                if not wfl_list.next_page_token:
                    break
        except libwes.ApiException as e:
            logger.error(e)
