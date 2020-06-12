import os
from unittest import TestCase
from unittest.mock import patch

from requests import HTTPError

from libiap import libgds
from . import _logger


class RestUnitTests(TestCase):

    @patch.dict(os.environ, clear=True)
    def test_iap_auth_token_none(self):
        try:
            next(libgds.list_files("does-not-matter", iap_base_url="DOES_NOT_MATTER"))
        except AssertionError as e:
            _logger.info(f"Raised AssertionError: {e}")
        self.assertRaises(AssertionError)

    @patch.dict(os.environ, clear=True)
    def test_iap_endpoint_none(self):
        try:
            next(libgds.list_files("does-not-matter", iap_auth_token="DOES_NOT_MATTER"))
        except AssertionError as e:
            _logger.info(f"Raised AssertionError: {e}")
        self.assertRaises(AssertionError)

    @patch.dict(os.environ, clear=True)
    @patch('libiap.rest.requests')
    def test_iap_auth_token_invalid(self, mock_requests):
        msg = "401 Client Error: Unauthorized for url: " \
              "https://aps2.platform.illumina.com/v1/files?pageSize=1000&volume.name=test"
        mock_requests.get.side_effect = HTTPError(msg)
        try:
            next(libgds.list_files("test", iap_base_url="https://aps2.platform.illumina.com", iap_auth_token="INVALID"))
        except HTTPError as e:
            _logger.info(f"Raised HTTPError: {e}")
        self.assertRaises(HTTPError)
