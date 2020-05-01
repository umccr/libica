import base64
import os
import random
import uuid
from datetime import datetime, timezone
from unittest import TestCase
from unittest.mock import Mock, patch

from mockito import mock, unstub, when

from libiap import libgds
from . import _rand, _logger


def _items(length=1):
    items = []
    volume_id = f"vol.{_rand(32)}"
    tenant_id = _rand(82)
    sub_tenant_id = "wid:" + str(uuid.uuid3(uuid.NAMESPACE_DNS, 'umccr.org'))
    created_by = str(uuid.uuid3(uuid.NAMESPACE_DNS, 'umccr.org'))
    modified_by = str(uuid.uuid3(uuid.NAMESPACE_DNS, 'umccr.org'))
    zulu_now = str(datetime.now(timezone.utc).isoformat()[:-6] + 'Z')
    for i in range(length):
        file_id = f"fil.{_rand(32)}"
        file_name = f"Test{i}.csv"
        path = f"/src/{file_name}"
        items.append(
            {
                "id": file_id,
                "name": file_name,
                "volumeId": volume_id,
                "volumeName": "workgroup-test",
                "tenantId": tenant_id,
                "subTenantId": sub_tenant_id,
                "path": path,
                "timeCreated": zulu_now,
                "createdBy": created_by,
                "timeModified": zulu_now,
                "modifiedBy": modified_by,
                "urn": f"urn:ilmn:iap:aps2:{tenant_id}:file:{file_id}#{path}",
                "sizeInBytes": random.randrange(1, 999999999999999999),
                "isUploaded": True,
                "archiveStatus": "None",
                "storageTier": "Standard"
            }
        )
    return items


def _folders(length, volume_name):
    folders = []
    volume_id = f"vol.{_rand(32)}"
    tenant_id = _rand(82)
    sub_tenant_id = "wid:" + str(uuid.uuid3(uuid.NAMESPACE_DNS, 'umccr.org'))
    created_by = str(uuid.uuid3(uuid.NAMESPACE_DNS, 'umccr.org'))
    modified_by = str(uuid.uuid3(uuid.NAMESPACE_DNS, 'umccr.org'))
    zulu_now = str(datetime.now(timezone.utc).isoformat()[:-6] + 'Z')
    for i in range(length):
        folder_id = f"fol.{_rand(32)}"
        folders.append(
            {
                "id": folder_id,
                "volumeId": volume_id,
                "volumeName": volume_name,
                "tenantId": tenant_id,
                "subTenantId": sub_tenant_id,
                "urn": f"urn:ilmn:iap:aps2:{tenant_id}:folder:{folder_id}#/",
                "path": "/",
                "acl": [
                    f"tid:{tenant_id}",
                    sub_tenant_id
                ],
                "timeCreated": zulu_now,
                "createdBy": created_by,
                "timeModified": zulu_now,
                "modifiedBy": modified_by,
                "jobStatus": "None"
            }
        )
    return folders


def _volumes(length=1):
    volumes = []
    tenant_id = _rand(82)
    sub_tenant_id = "wid:" + str(uuid.uuid3(uuid.NAMESPACE_DNS, 'umccr.org'))
    zulu_now = str(datetime.now(timezone.utc).isoformat()[:-6] + 'Z')
    for i in range(length):
        id = f"vol.{_rand(32)}"
        name = f"umccr-dev-{i}"
        volumes.append(
            {
                "id": id,
                "name": name,
                "tenantId": tenant_id,
                "subTenantId": sub_tenant_id,
                "urn": f"urn:ilmn:iap:aps2:{tenant_id}:volume:{id}#{name}",
                "timeCreated": zulu_now,
                "createdBy": str(uuid.uuid3(uuid.NAMESPACE_DNS, 'umccr.org')),
                "timeModified": zulu_now,
                "modifiedBy": str(uuid.uuid3(uuid.NAMESPACE_DNS, 'umccr.org'))
            }
        )
    return volumes


class LibGDSUnitTests(TestCase):

    def setUp(self) -> None:
        os.environ['IAP_BASE_URL'] = "mock"
        os.environ['IAP_AUTH_TOKEN'] = "mock"
        self.mock_response = mock(libgds.rest.requests.Response)
        self.mock_response.status_code = 200

    def tearDown(self) -> None:
        unstub()

    @patch.dict(os.environ, clear=True)
    @patch('libiap.rest.requests')
    def test_list_files(self, mock_requests):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = \
            {
                "items": _items(1),
                "itemCount": 1,
                "firstPageToken": base64.b64encode(b'doest-not-matter')
            }

        mock_requests.get.return_value = mock_response

        cnt = 0
        for file in libgds.list_files("does", iap_base_url="not", iap_auth_token="matter"):
            _logger.info(file)
            cnt += 1

        self.assertEqual(1, cnt)

    @patch.dict(os.environ, clear=True)
    @patch('libiap.rest.requests')
    def test_list_files_pagination(self, mock_requests):
        sampling = 2
        samples = _items(sampling)

        first_page_token = base64.b64encode(b'{"pageSize":2,"pageStartId":0,"pageEndId":1}')
        next_page_token = base64.b64encode(b'{"pageSize":2,"pageStartId":1,"pageEndId":2}')

        def _requests_get_side_effect(*args, **kwargs):
            # here kwargs.get('params') come from second keyword argument of requests GET API
            # i.e. requests.get(url, params={THIS_ONE}, **kwargs)
            # as we mock requests and introspecting inside of its side_effect at this point
            params = kwargs.get('params')
            _logger.info(params)

            if 'pageToken' not in params:
                mock_response_next_page = Mock()
                mock_response_next_page.status_code = 200
                mock_response_next_page.json.return_value = \
                    {
                        "items": samples[:1],
                        "itemCount": 1,
                        "firstPageToken": first_page_token,
                        "nextPageToken": next_page_token,
                    }
                return mock_response_next_page
            else:
                mock_response_last_page = Mock()
                mock_response_last_page.status_code = 200
                mock_response_last_page.json.return_value = \
                    {
                        "items": samples[1:],
                        "itemCount": 1,
                        "firstPageToken": first_page_token,
                        "prevPageToken": first_page_token,
                    }
                return mock_response_last_page

        mock_requests.get.side_effect = _requests_get_side_effect

        cnt = 0
        for file in libgds.list_files("does", iap_base_url="not", iap_auth_token="matter", page_size=2):
            _logger.info(file)
            cnt += 1

        self.assertEqual(sampling, cnt)

    @patch.dict(os.environ, clear=True)
    @patch('libiap.rest.requests')
    def test_get_file(self, mock_requests):
        file_id = f"fil.{_rand(32)}"
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"id": file_id}
        mock_requests.get.return_value = mock_response
        file = libgds.get_file("does", iap_base_url="not", iap_auth_token="matter")
        _logger.info(file)
        self.assertEqual(file_id, file.get("id"))

    # ---

    # All new test cases should use mockito

    def test_list_folders(self):
        self.mock_response.json = lambda: \
            {
                "items": _folders(1, volume_name="umccr-dev"),
                "itemCount": 1,
                "firstPageToken": base64.b64encode(b'doest-not-matter'),
            }
        when(libgds.rest.requests).get(...).thenReturn(self.mock_response)

        cnt = 0
        for folder in libgds.list_folders(volume_name="umccr-dev"):
            _logger.info(folder)
            cnt += 1

        self.assertEqual(1, cnt)

    def test_get_folder(self):
        folder_id = f"fol.{_rand(32)}"
        self.mock_response.json = lambda: {"id": folder_id}
        when(libgds.rest.requests).get(...).thenReturn(self.mock_response)
        folder = libgds.get_folder(folder_id=folder_id)
        _logger.info(folder)
        self.assertEqual(folder_id, folder.get("id"))

    def test_get_folder_session(self):
        # TODO pass-through for now
        folder_id = f"fol.{_rand(32)}"
        self.mock_response.json = lambda: {"id": folder_id}  # FIXME no idea how to mock folder session response
        when(libgds.rest.requests).get(...).thenReturn(self.mock_response)
        folder = libgds.get_folder_session(folder_id=folder_id, session_id="NO_IDEA_HOW_SESSION_ID_LOOK_ALIKE")
        _logger.info(folder)
        self.assertEqual(folder_id, folder.get("id"))

    def test_list_volumes(self):
        self.mock_response.json = lambda: \
            {
                "items": _volumes(1),
                "itemCount": 1,
                "firstPageToken": base64.b64encode(b'doest-not-matter'),
            }
        when(libgds.rest.requests).get(...).thenReturn(self.mock_response)

        cnt = 0
        for volume in libgds.list_volumes():
            _logger.info(volume)
            cnt += 1

        self.assertEqual(1, cnt)

    def test_get_volume(self):
        volume_id = f"vol.{_rand(32)}"
        self.mock_response.json = lambda: {"id": volume_id}
        when(libgds.rest.requests).get(...).thenReturn(self.mock_response)
        volume = libgds.get_volume(volume_id=volume_id)
        _logger.info(volume)
        self.assertEqual(volume_id, volume.get("id"))
