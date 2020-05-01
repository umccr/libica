import base64
import os
import random
import uuid
from datetime import datetime, timezone
from unittest import TestCase

from mockito import mock, when, unstub

from libiap import libens
from . import _rand, _logger


def _items(length=1):
    items = []
    sub_id = f"sub.{random.randint(1, 21) * 5}"
    tenant_id = _rand(82)
    created_by_user_id = str(uuid.uuid3(uuid.NAMESPACE_DNS, 'umccr.org'))
    zulu_now = str(datetime.now(timezone.utc).isoformat()[:-6] + 'Z')
    for i in range(length):
        items.append(
            {
                "id": sub_id,
                "urn": f"urn:ilmn:igp:us-east-1:{tenant_id}:subscription:{sub_id}",
                "type": "gds.files",
                "actions": [
                    "uploaded",
                    "deleted",
                    "archived",
                    "unarchived"
                ],
                "filterExpression": "",
                "name": "DataPortal",
                "description": "UMCCR GDS Files event subscription SQS queue delivery target",
                "deliveryTarget": {
                    "awsSqsQueue": {
                        "queueUrl": "https://sqs.ap-southeast-2.amazonaws.com/123456789/my-iap-ens-event-queue"
                    }
                },
                "tenantId": f"{tenant_id}",
                "createdByUserId": f"{created_by_user_id}",
                "timeCreated": f"{zulu_now}"
            }
        )
    return items


class LibENSUnitTests(TestCase):

    def setUp(self) -> None:
        os.environ['IAP_BASE_URL'] = "mock"
        os.environ['IAP_AUTH_TOKEN'] = "mock"
        self.mock_response = mock(spec=libens.rest.requests.Response)
        self.mock_response.status_code = 200

    def tearDown(self) -> None:
        unstub()

    def test_list_subscriptions(self):
        self.mock_response.json = lambda: \
            {
                "items": _items(1),
                "itemCount": 1,
                "firstPageToken": base64.b64encode(b'doest-not-matter'),
                "sortedBy": "id",
                "sortDirection": "Asc"
            }
        when(libens.rest.requests).get(...).thenReturn(self.mock_response)

        cnt = 0
        for sub in libens.list_subscriptions():
            _logger.info(sub)
            cnt += 1

        self.assertEqual(1, cnt)

    def test_get_subscription(self):
        sub_id = f"sub.{random.randint(1, 21) * 5}"
        self.mock_response.json = lambda: {"id": sub_id}
        when(libens.rest.requests).get(...).thenReturn(self.mock_response)
        sub = libens.get_subscription(subscription_id=sub_id)
        _logger.info(sub)
        self.assertEqual(sub_id, sub.get("id"))
