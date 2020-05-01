import base64
import os
import uuid
from datetime import datetime, timezone
from unittest import TestCase

from mockito import unstub, mock, when

from libiap import libtes
from . import _rand, _logger


def _tasks(length=1):
    items = []
    tenant_id = _rand(82)
    workgroup_id = str(uuid.uuid3(uuid.NAMESPACE_DNS, 'umccr.org'))
    created_by = str(uuid.uuid3(uuid.NAMESPACE_DNS, 'umccr.org'))
    modified_by = str(uuid.uuid3(uuid.NAMESPACE_DNS, 'umccr.org'))
    zulu_now = str(datetime.now(timezone.utc).isoformat()[:-6] + 'Z')
    for i in range(length):
        task_id = f"tdn.{_rand(32)}"
        items.append(
            {
                "id": task_id,
                "name": f"TSO500_NovaSeq_UMCCR_Prototype_{i}",
                "href": f"https://aps2.platform.illumina.com/v1/tasks/{task_id}",
                "acl": [
                    f"tid:{tenant_id}",
                    f"wid:{workgroup_id}"
                ],
                "tenantId": f"{tenant_id}",
                "subTenantId": f"{workgroup_id}",
                "createdBy": f"{created_by}",
                "timeCreated": f"{zulu_now}",
                "modifiedBy": f"{modified_by}",
                "timeModified": f"{zulu_now}"
            }
        )
    return items


def _runs(length=1):
    runs = []
    tenant_id = _rand(82)
    workgroup_id = str(uuid.uuid3(uuid.NAMESPACE_DNS, 'umccr.org'))
    created_by = str(uuid.uuid3(uuid.NAMESPACE_DNS, 'umccr.org'))
    modified_by = str(uuid.uuid3(uuid.NAMESPACE_DNS, 'umccr.org'))
    zulu_now = str(datetime.now(timezone.utc).isoformat()[:-6] + 'Z')
    for i in range(length):
        run_id = f"trn.{_rand(32)}"
        workflow_run_id = f"wfr.{_rand(32)}"
        task_version_number = f"tvn.{_rand(32)}"
        runs.append(
            {
                "id": run_id,
                "name": workflow_run_id,
                "href": f"https://aps2.platform.illumina.com/v1/tasks/runs/{run_id}",
                "description": f"TSO500 NovaSeq Prototype Demultiplex Task {i}",
                "status": "Failed",
                "taskVersionSummary": {
                    "id": task_version_number,
                    "version": "production",
                    "description": f"TSO500 NovaSeq Prototype Demultiplex Task {i}",
                    "acl": [
                        f"tid:{tenant_id}",
                        f"wid:{workgroup_id}"
                    ],
                    "tenantId": f"{tenant_id}",
                    "subTenantId": f"wid:{workgroup_id}",
                    "createdBy": f"{created_by}",
                    "timeCreated": f"{zulu_now}",
                    "modifiedBy": f"{modified_by}",
                    "timeModified": f"{zulu_now}"
                },
                "acl": [
                    f"tid:{tenant_id}",
                    f"wid:{workgroup_id}"
                ],
                "tenantId": f"{tenant_id}",
                "subTenantId": f"wid:{workgroup_id}",
                "createdBy": f"{created_by}",
                "timeCreated": f"{zulu_now}",
                "timeModified": f"{zulu_now}"
            }
        )
    return runs


def _versions(length=1):
    versions = []
    tenant_id = _rand(82)
    workgroup_id = str(uuid.uuid3(uuid.NAMESPACE_DNS, 'umccr.org'))
    created_by = str(uuid.uuid3(uuid.NAMESPACE_DNS, 'umccr.org'))
    modified_by = str(uuid.uuid3(uuid.NAMESPACE_DNS, 'umccr.org'))
    zulu_now = str(datetime.now(timezone.utc).isoformat()[:-6] + 'Z')
    for i in range(length):
        version_id = f"tvn.{_rand(32)}"
        task_id = f"tdn.{_rand(32)}"
        versions.append(
            {
                "id": version_id,
                "href": f"https://aps2.platform.illumina.com/v1/tasks/{task_id}/versions/{version_id}",
                "version": "production",
                "description": f"The TSO500 workflow has finished processing. An email has been sent. {i}",
                "acl": [
                    f"tid:{tenant_id}",
                    f"wid:{workgroup_id}"
                ],
                "tenantId": f"{tenant_id}",
                "subTenantId": f"wid:{workgroup_id}",
                "createdBy": f"{created_by}",
                "timeCreated": f"{zulu_now}",
                "modifiedBy": f"{modified_by}",
                "timeModified": f"{zulu_now}"
            }
        )
    return versions


class LibTESUnitTests(TestCase):

    def setUp(self) -> None:
        os.environ['IAP_BASE_URL'] = "mock"
        os.environ['IAP_AUTH_TOKEN'] = "mock"
        self.mock_response = mock(libtes.rest.requests.Response)
        self.mock_response.status_code = 200

    def tearDown(self) -> None:
        unstub()

    def test_list_tasks(self):
        self.mock_response.json = lambda: \
            {
                "items": _tasks(1),
                "itemCount": 1,
                "firstPageToken": base64.b64encode(b'doest-not-matter'),
                "lastPageToken": base64.b64encode(b'doest-not-matter'),
                "totalItemCount": 1,
                "totalPageCount": 1,
                "sortedBy": "TimeCreated",
                "sortDirection": "Asc"
            }
        when(libtes.rest.requests).get(...).thenReturn(self.mock_response)

        cnt = 0
        for task in libtes.list_tasks():
            _logger.info(task)
            cnt += 1

        self.assertEqual(1, cnt)

    def test_get_task(self):
        task_id = f"tdn.{_rand(32)}"
        self.mock_response.json = lambda: {"id": task_id}
        when(libtes.rest.requests).get(...).thenReturn(self.mock_response)
        task = libtes.get_task(task_id=task_id)
        _logger.info(task)
        self.assertEqual(task_id, task.get("id"))

    def test_list_task_runs(self):
        self.mock_response.json = lambda: \
            {
                "items": _runs(1),
                "itemCount": 1,
                "firstPageToken": base64.b64encode(b'doest-not-matter'),
                "lastPageToken": base64.b64encode(b'doest-not-matter'),
                "totalItemCount": 1,
                "totalPageCount": 1,
                "sortedBy": "TimeCreated",
                "sortDirection": "Asc"
            }
        when(libtes.rest.requests).get(...).thenReturn(self.mock_response)

        cnt = 0
        for run in libtes.list_task_runs():
            _logger.info(run)
            cnt += 1

        self.assertEqual(1, cnt)

    def test_get_task_run(self):
        run_id = f"trn.{_rand(32)}"
        self.mock_response.json = lambda: {"id": run_id}
        when(libtes.rest.requests).get(...).thenReturn(self.mock_response)
        task_run = libtes.get_task_run(run_id=run_id)
        _logger.info(task_run)
        self.assertEqual(run_id, task_run.get("id"))

    def test_list_task_versions(self):
        task_id = f"tdn.{_rand(32)}"
        self.mock_response.json = lambda: \
            {
                "items": _versions(1),
                "itemCount": 1,
                "firstPageToken": base64.b64encode(b'doest-not-matter'),
                "lastPageToken": base64.b64encode(b'doest-not-matter'),
                "totalItemCount": 1,
                "totalPageCount": 1,
                "sortedBy": "TimeCreated",
                "sortDirection": "Asc"
            }
        when(libtes.rest.requests).get(...).thenReturn(self.mock_response)

        cnt = 0
        for version in libtes.list_task_versions(task_id=task_id):
            _logger.info(version)
            cnt += 1

        self.assertEqual(1, cnt)

    def test_get_task_version(self):
        task_id = f"tdn.{_rand(32)}"
        version_id = f"tvn.{_rand(32)}"
        self.mock_response.json = lambda: {"id": version_id}
        when(libtes.rest.requests).get(...).thenReturn(self.mock_response)
        task_version = libtes.get_task_version(task_id=task_id, version_id=version_id)
        _logger.info(task_version)
        self.assertEqual(version_id, task_version.get("id"))
