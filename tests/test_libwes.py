import base64
import os
import uuid
from datetime import datetime, timezone
from unittest import TestCase

from mockito import unstub, mock, when

from libiap import libwes
from . import _rand, _logger


def _workflows(length=1):
    items = []
    tenant_id = _rand(82)
    workgroup_id = str(uuid.uuid3(uuid.NAMESPACE_DNS, 'umccr.org'))
    created_by = str(uuid.uuid3(uuid.NAMESPACE_DNS, 'umccr.org'))
    modified_by = str(uuid.uuid3(uuid.NAMESPACE_DNS, 'umccr.org'))
    zulu_now = str(datetime.now(timezone.utc).isoformat()[:-6] + 'Z')
    for i in range(length):
        workflow_id = f"wfl.{_rand(32)}"
        items.append(
            {
                "id": workflow_id,
                "href": f"https://aps2.platform.illumina.com/v1/workflows/{workflow_id}",
                "name": f"TSO500_NovaSeq_UMCCR_Prototype_Eval_ISL_Workflow {i}",
                "timeCreated": zulu_now,
                "timeModified": zulu_now,
                "createdBy": created_by,
                "modifiedBy": modified_by,
                "tenantId": tenant_id,
                "acl": [
                    f"tid:{tenant_id}",
                    f"wid:{workgroup_id}"
                ]
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
        run_id = f"wfr.{_rand(32)}"
        workflow_version_id = f"wfv.{_rand(32)}"
        workflow_id = f"wfl.{_rand(32)}"
        runs.append(
            {
                "id": run_id,
                "href": f"https://aps2.platform.illumina.com/v1/workflows/runs/{run_id}",
                "name": f"25100{i}_A00130_011{i}_ACGT{i}TCGAX",
                "timeStarted": zulu_now,
                "timeStopped": zulu_now,
                "status": "Succeeded",
                "statusSummary": "",
                "workflowVersion": {
                    "id": workflow_version_id,
                    "href": f"https://aps2.platform.illumina.com/v1/workflows/{workflow_id}/versions/production",
                    "version": "production",
                    "language": {
                        "name": "ISL"
                    },
                    "status": "Active",
                    "timeCreated": zulu_now,
                    "timeModified": zulu_now,
                    "createdBy": created_by,
                    "modifiedBy": modified_by,
                    "tenantId": tenant_id,
                    "acl": [
                        f"tid:{tenant_id}",
                        f"wid:{workgroup_id}"
                    ]
                },
                "timeCreated": zulu_now,
                "timeModified": zulu_now,
                "createdBy": created_by,
                "modifiedBy": modified_by,
                "tenantId": tenant_id,
                "acl": [
                    f"tid:{tenant_id}",
                    f"wid:{workgroup_id}"
                ]
            }
        )
    return runs


def _history():
    items = [
        {
            "eventId": 0,
            "eventType": "RunStarted",
            "timestamp": "2020-02-07T05:36:30.499938Z",
            "eventDetails": {}
        },
        {
            "eventId": 4,
            "previousEventId": 3,
            "eventType": "ActionStateEntered",
            "timestamp": "2020-02-07T05:36:30.8Z",
            "eventDetails": {
                "input": {},
                "stateName": "SetStartFromFastqFlag"
            }
        },
        {
            "eventId": 6,
            "previousEventId": 5,
            "eventType": "ActionStarted",
            "timestamp": "2020-02-07T05:36:31.048491Z",
            "eventDetails": {
                "actionParameters": {
                    "Result": {
                        "StartFromFastq": "false"
                    }
                },
                "stateName": "SetStartFromFastqFlag"
            }
        },
        {
            "eventId": 15,
            "previousEventId": 14,
            "eventType": "ActionStarted",
            "timestamp": "2020-02-07T05:36:31.649008Z",
            "eventDetails": {
                "actionParameters": {
                    "Result": {
                        "GdsPath": f"gds://umccr-gnr-test/wfr.{_rand(32)}/Demultiplex/Logs/FastqGeneration"
                    }
                },
                "stateName": "WorkflowDefinedFastqFolder"
            }
        }
    ]
    return items


def _all_versions():
    items = [
        {
            "id": f"wfv.{_rand(32)}",
            "href": f"https://aps2.platform.illumina.com/v1/workflows/wfl.{_rand(32)}/versions/production",
            "version": "production",
            "language": {
                "name": "ISL"
            },
            "status": "Active",
            "timeCreated": "2020-01-20T20:04:26.301694Z",
            "timeModified": "2020-01-20T20:04:26.301694Z",
            "createdBy": str(uuid.uuid3(uuid.NAMESPACE_DNS, 'umccr.org')),
            "modifiedBy": str(uuid.uuid3(uuid.NAMESPACE_DNS, 'umccr.org')),
            "tenantId": _rand(82),
            "acl": [
                f"tid:{_rand(82)}",
                f"wid:{str(uuid.uuid3(uuid.NAMESPACE_DNS, 'umccr.org'))}"
            ]
        },
        {
            "id": f"wfv.{_rand(32)}",
            "href": f"https://aps2.platform.illumina.com/v1/workflows/wfl.{_rand(32)}/versions/v1",
            "version": "v1",
            "language": {
                "name": "cwl"
            },
            "status": "Active",
            "timeCreated": "2020-02-13T03:44:16.768235Z",
            "timeModified": "2020-02-13T03:44:16.768235Z",
            "createdBy": "d24913a8-676f-39f3-9250-7cf22fbc48c8",
            "modifiedBy": "d24913a8-676f-39f3-9250-7cf22fbc48c8",
            "tenantId": _rand(82),
            "acl": [
                f"tid:{_rand(82)}",
                f"wid:{str(uuid.uuid3(uuid.NAMESPACE_DNS, 'umccr.org'))}"
            ]
        }
    ]
    return items


def _versions(length, workflow_id):
    versions = []
    tenant_id = _rand(82)
    workgroup_id = str(uuid.uuid3(uuid.NAMESPACE_DNS, 'umccr.org'))
    created_by = str(uuid.uuid3(uuid.NAMESPACE_DNS, 'umccr.org'))
    modified_by = str(uuid.uuid3(uuid.NAMESPACE_DNS, 'umccr.org'))
    zulu_now = str(datetime.now(timezone.utc).isoformat()[:-6] + 'Z')
    for i in range(length):
        version_id = f"wfv.{_rand(32)}"
        versions.append(
            {
                "id": version_id,
                "href": f"https://aps2.platform.illumina.com/v1/workflows/{workflow_id}/versions/v1",
                "version": "v1",
                "language": {
                    "name": "cwl"
                },
                "status": "Active",
                "timeCreated": zulu_now,
                "timeModified": zulu_now,
                "createdBy": created_by,
                "modifiedBy": modified_by,
                "tenantId": tenant_id,
                "acl": [
                    f"tid:{tenant_id}",
                    f"wid:{workgroup_id}"
                ]
            }
        )
    return versions


class LibWESUnitTests(TestCase):

    def setUp(self) -> None:
        os.environ['IAP_BASE_URL'] = "mock"
        os.environ['IAP_AUTH_TOKEN'] = "mock"
        self.mock_response = mock(libwes.rest.requests.Response)
        self.mock_response.status_code = 200

    def tearDown(self) -> None:
        unstub()

    def test_list_workflows(self):
        self.mock_response.json = lambda: \
            {
                "items": _workflows(1),
                "itemCount": 1,
                "firstPageToken": base64.b64encode(b'doest-not-matter'),
            }
        when(libwes.rest.requests).get(...).thenReturn(self.mock_response)

        cnt = 0
        for workflow in libwes.list_workflows():
            _logger.info(workflow)
            cnt += 1

        self.assertEqual(1, cnt)

    def test_get_workflow(self):
        workflow_id = f"wfl.{_rand(32)}"
        self.mock_response.json = lambda: {"id": workflow_id}
        when(libwes.rest.requests).get(...).thenReturn(self.mock_response)
        workflow = libwes.get_workflow(workflow_id=workflow_id)
        _logger.info(workflow)
        self.assertEqual(workflow_id, workflow.get("id"))

    def test_list_workflow_runs(self):
        self.mock_response.json = lambda: \
            {
                "items": _runs(1),
                "itemCount": 1,
                "firstPageToken": base64.b64encode(b'doest-not-matter'),
            }
        when(libwes.rest.requests).get(...).thenReturn(self.mock_response)

        cnt = 0
        for workflow in libwes.list_workflow_runs():
            _logger.info(workflow)
            cnt += 1

        self.assertEqual(1, cnt)

    def test_get_workflow_run(self):
        run_id = f"wfr.{_rand(32)}"
        self.mock_response.json = lambda: {"id": run_id}
        when(libwes.rest.requests).get(...).thenReturn(self.mock_response)
        workflow_run = libwes.get_workflow_run(run_id=run_id)
        _logger.info(workflow_run)
        self.assertEqual(run_id, workflow_run.get("id"))

    def test_list_workflow_run_history(self):
        run_id = f"wfr.{_rand(32)}"
        self.mock_response.json = lambda: \
            {
                "items": _history(),
                "itemCount": 1,
                "firstPageToken": base64.b64encode(b'doest-not-matter'),
            }
        when(libwes.rest.requests).get(...).thenReturn(self.mock_response)

        cnt = 0
        for history in libwes.list_workflow_run_history(run_id=run_id):
            _logger.info(history)
            cnt += 1

        self.assertEqual(len(_history()), cnt)

    def test_list_signals(self):
        self.mock_response.json = lambda: \
            {
                "items": [],
                "itemCount": 0,
                "firstPageToken": base64.b64encode(b'doest-not-matter'),
            }
        when(libwes.rest.requests).get(...).thenReturn(self.mock_response)

        cnt = 0
        for signal in libwes.list_signals():
            _logger.info(signal)
            cnt += 1

        self.assertEqual(0, cnt)

    def test_get_signal(self):
        # TODO no sample response structure for signal yet
        pass

    def test_list_all_workflow_versions(self):
        self.mock_response.json = lambda: \
            {
                "items": _all_versions(),
                "itemCount": 1,
                "firstPageToken": base64.b64encode(b'doest-not-matter'),
            }
        when(libwes.rest.requests).get(...).thenReturn(self.mock_response)

        cnt = 0
        for version in libwes.list_all_workflow_versions():
            _logger.info(version)
            cnt += 1

        self.assertEqual(len(_all_versions()), cnt)

    def test_list_workflow_versions(self):
        workflow_id = f"wfl.{_rand(32)}"
        self.mock_response.json = lambda: \
            {
                "items": _versions(1, workflow_id),
                "itemCount": 1,
                "firstPageToken": base64.b64encode(b'doest-not-matter'),
            }
        when(libwes.rest.requests).get(...).thenReturn(self.mock_response)

        cnt = 0
        for version in libwes.list_workflow_versions(workflow_id=workflow_id):
            _logger.info(version)
            cnt += 1

        self.assertEqual(1, cnt)

    def test_get_workflow_version(self):
        workflow_version_id = f"wfv.{_rand(32)}"
        self.mock_response.json = lambda: {"id": workflow_version_id, "version": "v1"}
        when(libwes.rest.requests).get(...).thenReturn(self.mock_response)
        version = libwes.get_workflow_version(workflow_id=workflow_version_id, version_name="v1")
        _logger.info(version)
        self.assertEqual(workflow_version_id, version.get("id"))
        self.assertEqual("v1", version.get("version"))
