# coding: utf-8

"""
    Genomic Data Store Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import libica.openapi.libgds
from libica.openapi.libgds.models.aws_s3_presigned_url_for_upload import AwsS3PresignedUrlForUpload  # noqa: E501
from libica.openapi.libgds.rest import ApiException

class TestAwsS3PresignedUrlForUpload(unittest.TestCase):
    """AwsS3PresignedUrlForUpload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AwsS3PresignedUrlForUpload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = libica.openapi.libgds.models.aws_s3_presigned_url_for_upload.AwsS3PresignedUrlForUpload()  # noqa: E501
        if include_optional :
            return AwsS3PresignedUrlForUpload(
                single_part_url = '0', 
                multipart_template = '0', 
                multipart_signatures = [
                    libica.openapi.libgds.models.part_info.PartInfo(
                        part = 56, 
                        date = '0', 
                        date_time = '0', 
                        signature = '0', )
                    ], 
                multipart_upload_id = '0', 
                server_side_encryption_algorithm = '0', 
                server_side_encryption_key = '0'
            )
        else :
            return AwsS3PresignedUrlForUpload(
        )

    def testAwsS3PresignedUrlForUpload(self):
        """Test AwsS3PresignedUrlForUpload"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
