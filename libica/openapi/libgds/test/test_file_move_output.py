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
from libica.openapi.libgds.models.file_move_output import FileMoveOutput  # noqa: E501
from libica.openapi.libgds.rest import ApiException

class TestFileMoveOutput(unittest.TestCase):
    """FileMoveOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FileMoveOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = libica.openapi.libgds.models.file_move_output.FileMoveOutput()  # noqa: E501
        if include_optional :
            return FileMoveOutput(
                items_skipped_count = 56, 
                items_failed_count = 56, 
                items_moved_count = 56, 
                folders_moved_count = 56, 
                elastic_indexing_matched = True, 
                items_failed = [
                    libica.openapi.libgds.models.bulk_failed_item.BulkFailedItem(
                        id = '0', 
                        error_response = libica.openapi.libgds.models.error_response.ErrorResponse(
                            code = '0', 
                            message = '0', 
                            details = [
                                None
                                ], ), )
                    ]
            )
        else :
            return FileMoveOutput(
        )

    def testFileMoveOutput(self):
        """Test FileMoveOutput"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()