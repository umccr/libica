# coding: utf-8

"""
    Workflow Execution Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import libiap.openapi.libwes
from libiap.openapi.libwes.models.workflow_signal_compact import WorkflowSignalCompact  # noqa: E501
from libiap.openapi.libwes.rest import ApiException

class TestWorkflowSignalCompact(unittest.TestCase):
    """WorkflowSignalCompact unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test WorkflowSignalCompact
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = libiap.openapi.libwes.models.workflow_signal_compact.WorkflowSignalCompact()  # noqa: E501
        if include_optional :
            return WorkflowSignalCompact(
                id = '0', 
                urn = '0', 
                href = '0', 
                send_heartbeat_href = '0', 
                send_success_response_href = '0', 
                send_failure_response_href = '0', 
                name = '0', 
                status = '0', 
                type = '0', 
                description = '0', 
                inputs = None, 
                workflow_run = libiap.openapi.libwes.models.workflow_run_compact.WorkflowRunCompact(
                    id = '0', 
                    urn = '0', 
                    href = '0', 
                    name = '0', 
                    time_started = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    time_stopped = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    status = '0', 
                    status_summary = '0', 
                    error = '0', 
                    error_cause = '0', 
                    workflow_version = libiap.openapi.libwes.models.workflow_version_compact.WorkflowVersionCompact(
                        id = '0', 
                        urn = '0', 
                        href = '0', 
                        version = '0', 
                        category = '0', 
                        description = '0', 
                        language = libiap.openapi.libwes.models.workflow_language.WorkflowLanguage(
                            name = '0', 
                            version = '0', ), 
                        status = '0', 
                        created_by_client_id = '0', 
                        time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        created_by = '0', 
                        modified_by = '0', 
                        tenant_id = '0', 
                        acl = [
                            '0'
                            ], ), 
                    created_by_client_id = '0', 
                    time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    created_by = '0', 
                    modified_by = '0', 
                    tenant_id = '0', 
                    acl = [
                        '0'
                        ], ), 
                timeout_seconds = 56, 
                result = None, 
                error = '0', 
                error_cause = '0', 
                created_by_client_id = '0', 
                time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                created_by = '0', 
                modified_by = '0', 
                tenant_id = '0', 
                acl = [
                    '0'
                    ]
            )
        else :
            return WorkflowSignalCompact(
        )

    def testWorkflowSignalCompact(self):
        """Test WorkflowSignalCompact"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
