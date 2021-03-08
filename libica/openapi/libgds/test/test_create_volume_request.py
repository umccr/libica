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
from libica.openapi.libgds.models.create_volume_request import CreateVolumeRequest  # noqa: E501
from libica.openapi.libgds.rest import ApiException

class TestCreateVolumeRequest(unittest.TestCase):
    """CreateVolumeRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateVolumeRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = libica.openapi.libgds.models.create_volume_request.CreateVolumeRequest()  # noqa: E501
        if include_optional :
            return CreateVolumeRequest(
                name = '0', 
                volume_configuration_name = '0', 
                # root_key_prefix = 'a'
            )
        else :
            return CreateVolumeRequest(
                name = '0',
        )

    def testCreateVolumeRequest(self):
        """Test CreateVolumeRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
