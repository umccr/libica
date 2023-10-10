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
from libica.openapi.libgds.models.file_move_operation_parameters import FileMoveOperationParameters  # noqa: E501
from libica.openapi.libgds.rest import ApiException

class TestFileMoveOperationParameters(unittest.TestCase):
    """FileMoveOperationParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FileMoveOperationParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = libica.openapi.libgds.models.file_move_operation_parameters.FileMoveOperationParameters()  # noqa: E501
        if include_optional :
            return FileMoveOperationParameters(
                source_volume_id = '0', 
                source_file_ids = [
                    '0'
                    ], 
                target_folder_id = '0'
            )
        else :
            return FileMoveOperationParameters(
        )

    def testFileMoveOperationParameters(self):
        """Test FileMoveOperationParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
