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

import libiap.openapi.libgds
from libiap.openapi.libgds.models.folder_writeable_response import FolderWriteableResponse  # noqa: E501
from libiap.openapi.libgds.rest import ApiException

class TestFolderWriteableResponse(unittest.TestCase):
    """FolderWriteableResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FolderWriteableResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = libiap.openapi.libgds.models.folder_writeable_response.FolderWriteableResponse()  # noqa: E501
        if include_optional :
            return FolderWriteableResponse(
                id = '0', 
                name = '0', 
                volume_id = '0', 
                volume_name = '0', 
                tenant_id = '0', 
                sub_tenant_id = '0', 
                urn = '0', 
                path = '0', 
                acl = [
                    '0'
                    ], 
                inherited_acl = [
                    '0'
                    ], 
                time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                created_by = '0', 
                time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                modified_by = '0', 
                metadata = None, 
                job_status = 'None', 
                archive_job_storage_tier = 'None', 
                object_store_access = libiap.openapi.libgds.models.object_store_access.ObjectStoreAccess(
                    session_id = '0', 
                    aws_s3_temporary_upload_credentials = libiap.openapi.libgds.models.aws_s3_temporary_upload_credentials.AwsS3TemporaryUploadCredentials(
                        access_key_id = '0', 
                        secret_access_key = '0', 
                        session_token = '0', 
                        region = '0', 
                        bucket_name = '0', 
                        key_prefix = '0', 
                        expiration_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        service_url = '0', ), )
            )
        else :
            return FolderWriteableResponse(
        )

    def testFolderWriteableResponse(self):
        """Test FolderWriteableResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
