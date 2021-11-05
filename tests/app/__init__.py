import logging
import os
import warnings
from unittest import TestCase

from mockito import unstub

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class IcaUnitTests(TestCase):

    def setUp(self) -> None:
        super(IcaUnitTests, self).setUp()
        os.environ['ICA_BASE_URL'] = "http://localhost"
        os.environ['ICA_ACCESS_TOKEN'] = "mock"

        # filter dependencies unclose socket warning
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

    def tearDown(self) -> None:
        del os.environ['ICA_BASE_URL']
        del os.environ['ICA_ACCESS_TOKEN']
        unstub()

    def verify_local(self):
        logger.info(f"ICA_BASE_URL={os.getenv('ICA_BASE_URL')}")
        assert os.environ['ICA_BASE_URL'] == "http://localhost"
        assert os.environ['ICA_ACCESS_TOKEN'] == "mock"
        self.assertEqual(os.environ['ICA_BASE_URL'], "http://localhost")


class IcaIntegrationTests(TestCase):

    def setUp(self) -> None:
        super(IcaIntegrationTests, self).setUp()

        # turn dependencies logger off
        logging.getLogger('boto3').setLevel(logging.CRITICAL)
        logging.getLogger('botocore').setLevel(logging.CRITICAL)
        logging.getLogger('nose').setLevel(logging.CRITICAL)
        logging.getLogger('s3transfer').setLevel(logging.CRITICAL)
        logging.getLogger('urllib3').setLevel(logging.CRITICAL)

        # filter dependencies unclose socket warning
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
