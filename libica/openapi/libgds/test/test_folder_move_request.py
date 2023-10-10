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
from libica.openapi.libgds.models.folder_move_request import FolderMoveRequest  # noqa: E501
from libica.openapi.libgds.rest import ApiException

class TestFolderMoveRequest(unittest.TestCase):
    """FolderMoveRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FolderMoveRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = libica.openapi.libgds.models.folder_move_request.FolderMoveRequest()  # noqa: E501
        if include_optional :
            return FolderMoveRequest(
                target_parent_folder_id = '0'
            )
        else :
            return FolderMoveRequest(
                target_parent_folder_id = '0',
        )

    def testFolderMoveRequest(self):
        """Test FolderMoveRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
