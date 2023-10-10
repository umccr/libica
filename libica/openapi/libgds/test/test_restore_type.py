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
from libica.openapi.libgds.models.restore_type import RestoreType  # noqa: E501
from libica.openapi.libgds.rest import ApiException

class TestRestoreType(unittest.TestCase):
    """RestoreType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RestoreType
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = libica.openapi.libgds.models.restore_type.RestoreType()  # noqa: E501
        if include_optional :
            return RestoreType(
            )
        else :
            return RestoreType(
        )

    def testRestoreType(self):
        """Test RestoreType"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
