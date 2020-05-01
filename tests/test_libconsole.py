import os
import uuid
from unittest import TestCase

from mockito import unstub, mock, when

from libiap import libconsole
from . import _rand, _logger


class LibConsoleUnitTests(TestCase):

    def setUp(self) -> None:
        os.environ['IAP_BASE_URL'] = "mock"
        os.environ['IAP_AUTH_TOKEN'] = "mock"
        self.mock_response = mock(spec=libconsole.rest.requests.Response)
        self.mock_response.status_code = 200

    def tearDown(self) -> None:
        unstub()

    def test_get_service_health(self):
        self.mock_response.json = lambda: \
            {
                "status": "Healthy",
                "details": [
                    {
                        "name": "Developer Console Service",
                        "status": "Healthy",
                        "version": "0.1.0"
                    },
                    {
                        "name": "GenomicDataStore",
                        "status": "Healthy",
                        "version": "0.1.0"
                    },
                    {
                        "name": "TaskExecutionService",
                        "status": "Healthy",
                        "version": "0.1.0"
                    },
                    {
                        "name": "EventNotificationService",
                        "status": "Healthy",
                        "version": "0.1.0"
                    },
                    {
                        "name": "WorkflowExecutionService",
                        "status": "Healthy",
                        "version": "0.1.0"
                    }
                ]
            }
        when(libconsole.rest.requests).get(...).thenReturn(self.mock_response)
        health = libconsole.get_service_health()
        _logger.info(health)
        self.assertEqual(health['status'], "Healthy")

    def test_list_regions(self):
        self.mock_response.json = lambda: []
        when(libconsole.rest.requests).get(...).thenReturn(self.mock_response)
        regions = libconsole.list_regions()
        _logger.info(regions)
        self.assertEqual(len(regions), 0)

    def test_get_account(self):
        account_id = str(uuid.uuid3(uuid.NAMESPACE_DNS, 'umccr.org'))
        self.mock_response.json = lambda: \
            {
                "id": account_id,
                "type": "User",
                "name": "John Doe",
                "domain": {
                    "id": _rand(82),
                    "name": "umccr"
                }
            }
        when(libconsole.rest.requests).get(...).thenReturn(self.mock_response)
        account = libconsole.get_account(account_id=account_id)
        _logger.info(account)
        self.assertEqual(account_id, account['id'])

    def test_get_token_details(self):
        account_id = str(uuid.uuid3(uuid.NAMESPACE_DNS, 'umccr.org'))
        tenant_id = _rand(82)
        self.mock_response.json = lambda: \
            {
                "uid": account_id,
                "name": "John Doe",
                "username": "john.doe@example.org",
                "tid": tenant_id,
                "acls": [
                    f"uid:{account_id}",
                    f"tid:{tenant_id}"
                ]
            }
        when(libconsole.rest.requests).get(...).thenReturn(self.mock_response)
        token_details = libconsole.get_token_details(account_id=account_id)
        _logger.info(token_details)
        self.assertEqual(account_id, token_details['uid'])

    def test_get_usage(self):
        self.mock_response.json = lambda: \
            {
                "items": [
                    {
                        "start": "2022-02-27T00:00:00Z",
                        "end": "2022-04-24T23:59:59Z",
                        "iCredit": 999,
                        "totalUsages": [],
                        "userAggregatedUsages": []
                    }
                ]
            }
        when(libconsole.rest.requests).get(...).thenReturn(self.mock_response)
        usage = libconsole.get_usage()
        _logger.info(usage)
        self.assertIsNotNone(usage)

    def test_get_usage_details(self):
        self.mock_response.json = lambda: \
            {
                "start": "04/27/2020",
                "end": "05/24/2020",
                "computeUsages": [],
                "gdsUsages": []
            }
        when(libconsole.rest.requests).get(...).thenReturn(self.mock_response)
        usage_details = libconsole.get_usage_details()
        _logger.info(usage_details)
        self.assertIsNotNone(usage_details)
