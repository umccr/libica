import logging
import os
import time
from contextlib import closing
from unittest import TestCase

from libiap.openapi import libwes
from libiap.openapi.libwes import WorkflowList, WorkflowCompact, Workflow
from tests.integration.prism import MockServer

logger = logging.getLogger(__name__)


class LibWESIntegrationTests(TestCase):

    _srv = None

    @classmethod
    def setUpClass(cls) -> None:
        super(LibWESIntegrationTests, cls).setUpClass()

        cls.iap_auth_token = os.getenv("IAP_AUTH_TOKEN", None)
        cls.iap_base_url = os.getenv("IAP_BASE_URL", None)

        if cls.iap_auth_token is None or cls.iap_base_url is None:
            cls._srv = MockServer("prism mock -d swagger/wes.json")
            cls._srv.start()
            while not cls._srv.ready:
                time.sleep(1)
            cls.iap_base_url = "http://0.0.0.0:4010"
            cls.iap_auth_token = "MOCK"

        assert cls.iap_auth_token is not None, "IAP_AUTH_TOKEN is not defined"
        assert cls.iap_base_url is not None, "IAP_BASE_URL is not defined"

    @classmethod
    def tearDownClass(cls) -> None:
        if cls._srv is not None:
            cls._srv.stop()

    def setUp(self) -> None:
        super(LibWESIntegrationTests, self).setUp()

        self.configuration = libwes.Configuration(
            host=f"{self.iap_base_url}",
            api_key={
                'Authorization': f"{self.iap_auth_token}"
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
                wfl_list: WorkflowList = wfl_api.list_workflows(page_size=100, page_token=page_token)
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
