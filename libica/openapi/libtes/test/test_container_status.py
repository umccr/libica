# coding: utf-8

"""
    Task Execution Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import libica.openapi.libtes
from libica.openapi.libtes.models.container_status import ContainerStatus  # noqa: E501
from libica.openapi.libtes.rest import ApiException

class TestContainerStatus(unittest.TestCase):
    """ContainerStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ContainerStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = libica.openapi.libtes.models.container_status.ContainerStatus()  # noqa: E501
        if include_optional :
            return ContainerStatus(
                name = '0', 
                state = libica.openapi.libtes.models.container_state.ContainerState(
                    waiting = libica.openapi.libtes.models.container_state_waiting.ContainerStateWaiting(
                        reason = '0', 
                        message = '0', ), 
                    running = libica.openapi.libtes.models.container_state_running.ContainerStateRunning(
                        started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    terminated = libica.openapi.libtes.models.container_state_terminated.ContainerStateTerminated(
                        exit_code = 56, 
                        signal = 56, 
                        reason = '0', 
                        message = '0', 
                        started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        finished_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        container_id = '0', ), )
            )
        else :
            return ContainerStatus(
        )

    def testContainerStatus(self):
        """Test ContainerStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
