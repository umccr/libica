import base64
import os
import random
import string
import uuid
from datetime import datetime, timezone
from unittest import TestCase, skip
from unittest.mock import Mock, patch

from requests import HTTPError

from libiap import libgds
from .log import logger


def _rand(length=8):
    alpha_numeric = string.ascii_letters + string.digits
    return ''.join((random.choice(alpha_numeric) for i in range(length)))


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


class LibGDSUnitTests(TestCase):

    @patch.dict(os.environ, clear=True)
    def test_iap_auth_token_none(self):
        try:
            next(libgds.list_files("does-not-matter", iap_base_url="DOES_NOT_MATTER"))
        except AssertionError as e:
            logger.info(f"Raised AssertionError: {e}")
        self.assertRaises(AssertionError)

    @patch.dict(os.environ, clear=True)
    def test_iap_endpoint_none(self):
        try:
            next(libgds.list_files("does-not-matter", iap_auth_token="DOES_NOT_MATTER"))
        except AssertionError as e:
            logger.info(f"Raised AssertionError: {e}")
        self.assertRaises(AssertionError)

    @patch.dict(os.environ, clear=True)
    @patch('libiap.libgds.requests')
    def test_iap_auth_token_invalid(self, mock_requests):
        msg = "401 Client Error: Unauthorized for url: " \
              "https://aps2.platform.illumina.com/v1/files?pageSize=1000&volume.name=test"
        mock_requests.get.side_effect = HTTPError(msg)
        try:
            next(libgds.list_files("test", iap_base_url="https://aps2.platform.illumina.com", iap_auth_token="INVALID"))
        except HTTPError as e:
            logger.info(f"Raised HTTPError: {e}")
        self.assertRaises(HTTPError)

    @patch.dict(os.environ, clear=True)
    @patch('libiap.libgds.requests')
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
            logger.info(file)
            cnt += 1

        self.assertEqual(1, cnt)

    @patch.dict(os.environ, clear=True)
    @patch('libiap.libgds.requests')
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
            logger.info(params)

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
            logger.info(file)
            cnt += 1

        self.assertEqual(sampling, cnt)

    @patch.dict(os.environ, clear=True)
    @patch('libiap.libgds.requests')
    def test_get_file(self, mock_requests):
        file_id = f"fil.{_rand(32)}"
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"id": file_id}
        mock_requests.get.return_value = mock_response
        file = libgds.get_file("does", iap_base_url="not", iap_auth_token="matter")
        logger.info(file)
        self.assertEqual(file_id, file.get("id"))

    @skip(reason="Skip for local test only")
    def test_list_files_local(self):
        """
        To test it locally, comment @skip and do as follows:
        export IAP_BASE_URL=<baseUrl>
        export IAP_AUTH_TOKEN=<tok>
        export IAP_GDS_VOLUME=<volName>
        python -m unittest tests.test_libgds.LibGDSUnitTests.test_list_files_local > out.log
        """
        iap_gds_volume = os.getenv('IAP_GDS_VOLUME', None)
        assert iap_gds_volume is not None, "IAP_GDS_VOLUME is not defined"
        for file in libgds.list_files(volume_name=iap_gds_volume):
            print(file)
        self.assertTrue(iap_gds_volume)

    @skip(reason="Skip for local test only")
    def test_get_file_local(self):
        """
        To test it locally, comment @skip and do as follows:
        export IAP_BASE_URL=<baseUrl>
        export IAP_AUTH_TOKEN=<tok>
        export IAP_GDS_FILE=<fileId>
        python -m unittest tests.test_libgds.LibGDSUnitTests.test_get_file_local > out.log
        """
        iap_gds_file = os.getenv('IAP_GDS_FILE', None)
        assert iap_gds_file is not None, "IAP_GDS_FILE is not defined"
        print(libgds.get_file(file_id=iap_gds_file))
        self.assertTrue(iap_gds_file)

    @skip(reason="Skip for local test only")
    def test_list_volumes_local(self):
        """
        To test it locally, comment @skip and do as follows:
        export IAP_BASE_URL=<baseUrl>
        export IAP_AUTH_TOKEN=<tok>
        python -m unittest tests.test_libgds.LibGDSUnitTests.test_list_volumes_local > out.log
        """
        for file in libgds.list_volumes(page_size=10):
            print(file)
        self.assertTrue(os.getenv('IAP_AUTH_TOKEN'))

    @skip(reason="Skip for local test only")
    def test_get_volume_local(self):
        """
        To test it locally, comment @skip and do as follows:
        export IAP_BASE_URL=<baseUrl>
        export IAP_AUTH_TOKEN=<tok>
        export IAP_GDS_VOLUME=<volId>  <-- Caveats: API doc say volume_id but volume_name seem to be working, yikes!
        python -m unittest tests.test_libgds.LibGDSUnitTests.test_get_volume_local > out.log
        """
        iap_gds_volume = os.getenv('IAP_GDS_VOLUME', None)
        assert iap_gds_volume is not None, "IAP_GDS_VOLUME is not defined"
        print(libgds.get_volume(volume_id=iap_gds_volume))
        self.assertTrue(iap_gds_volume)
