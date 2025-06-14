# coding: utf-8

"""
    ICA Rest API

    This API can be used to interact with Illumina Connected Analytics.<br> <h2>Authentication</h2> <p> Authentication to the  API can be done in multiple ways:<br> <ul><li>For the entire API, except for the POST /tokens endpoint: API-key + JWT</li> <li>Only for the POST /tokens endpoint: API-key + Basic Authentication</li></ul> </p> <p> <h4>API-key</h4> API keys are managed within the Illumina portal where you can manage your profile after you have logged on. The API-key has to be provided in the X-API-Key header parameter when executing API calls to ICA. In the background, a JWT will be requested at the IDP of Illumina to create a session. A good practice is to not use the API-key for every API call, but to first generate a JWT and to use that for authentication in subsequent calls.<br> </p> <p> <h4>JWT</h4> To avoid using an API-key for each call, we recommend to request a JWT via the POST /tokens endpoint  using this API-key. The JWT will expire after a pre-configured period specified by a tenant administrator through the IAM console in the Illumina portal. The JWT is the preferred way for authentication.<br>A not yet expired, still valid JWT could be refreshed using the POST /tokens:refresh endpoint.<br>Refreshing the JWT is not possible if the JWT was generated by using an API-key.<br> </p> <p> <h4>Basic Authentication</h4> Basic authentication is only supported by the POST /tokens endpoint for generating a JWT. Use \"Basic base64encoded(emailaddress:password)\" in the \"Authorization\" header parameter for this authentication method. In case having access to multiple tenants using the same email-address, also provide the \"tenant\" request parameter to indicate what tenant you would like to request a JWT for. </p> <p> <h2>Compression</h2> If the API client provides request header 'Accept-Encoding' with value 'gzip', then the API applies GZIP compression on the JSON response. This significantly reduces the size and thus the download time of the response, which results in faster end-to-end API calls. In case of compression, the API also provides response header 'Content-Encoding' with value 'gzip', as indication for the client that decompression is required. </p> 

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from libica.openapi.v3.models.data_transfer import DataTransfer

class TestDataTransfer(unittest.TestCase):
    """DataTransfer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataTransfer:
        """Test DataTransfer
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataTransfer`
        """
        model = DataTransfer()
        if include_optional:
            return DataTransfer(
                id = '',
                time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                owner_id = '',
                tenant_id = '',
                tenant_name = '',
                reference = '0',
                direction = 'UPLOAD',
                connector = libica.openapi.v3.models.connector.Connector(
                    id = '', 
                    time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    owner_id = '', 
                    tenant_id = '', 
                    tenant_name = '', 
                    code = '0', 
                    active = True, 
                    connected = True, 
                    technical_code = '0', 
                    initialization_key = '0', 
                    description = '', 
                    mode = 'DOWNLOAD', 
                    max_bandwidth = 0.01, 
                    max_concurrent_transfers = 1, 
                    os = 'WINDOWS', 
                    installation_status = 'PENDING_INSTALLATION', 
                    new_connector_version_available = True, ),
                protocol = 'HTTPS',
                data_transferred = 0,
                status = 'REQUESTED',
                status_message = '0',
                duration = 0,
                project = libica.openapi.v3.models.project.Project(
                    id = '', 
                    time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    owner_id = '', 
                    tenant_id = '', 
                    tenant_name = '', 
                    urn = '0', 
                    name = '0', 
                    active = True, 
                    base_enabled = True, 
                    short_description = '0', 
                    information = '', 
                    region = libica.openapi.v3.models.region.Region(
                        id = '', 
                        time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        owner_id = '', 
                        tenant_id = '', 
                        tenant_name = '', 
                        code = '0', 
                        country = libica.openapi.v3.models.country.Country(
                            id = '', 
                            time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            owner_id = '', 
                            tenant_id = '', 
                            tenant_name = '', 
                            code = '', 
                            name = '', 
                            region = '', ), 
                        city_name = '0', ), 
                    billing_mode = 'PROJECT', 
                    data_sharing_enabled = True, 
                    tags = libica.openapi.v3.models.project_tag.ProjectTag(
                        technical_tags = [
                            ''
                            ], 
                        user_tags = [
                            ''
                            ], ), 
                    storage_bundle = libica.openapi.v3.models.storage_bundle.StorageBundle(
                        id = '', 
                        time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        owner_id = '', 
                        tenant_id = '', 
                        tenant_name = '', 
                        bundle_name = '0', 
                        entitlement_name = '0', 
                        region = libica.openapi.v3.models.region.Region(
                            id = '', 
                            time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            owner_id = '', 
                            tenant_id = '', 
                            tenant_name = '', 
                            code = '0', 
                            country = libica.openapi.v3.models.country.Country(
                                id = '', 
                                time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                owner_id = '', 
                                tenant_id = '', 
                                tenant_name = '', 
                                code = '', 
                                name = '', 
                                region = '', ), 
                            city_name = '0', ), ), 
                    self_managed_storage_configuration = libica.openapi.v3.models.storage_configuration.StorageConfiguration(
                        id = '', 
                        time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        owner_id = '', 
                        tenant_id = '', 
                        tenant_name = '', 
                        name = '', 
                        description = '', 
                        type = 'AWS_S3', 
                        status = 'INITIALIZING', 
                        error_message = '', 
                        region = , 
                        is_default = True, ), 
                    analysis_priority = 'LOW', 
                    metadata_model = libica.openapi.v3.models.metadata_model.MetadataModel(
                        id = '', 
                        time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        owner_id = '', 
                        tenant_id = '', 
                        tenant_name = '', 
                        name = '0', 
                        description = '', 
                        state = 'DRAFT', 
                        parent_model_id = '', ), 
                    application = libica.openapi.v3.models.application.Application(
                        id = '', 
                        name = '', 
                        type = 'MAIN', 
                        display_name = '', ), ),
                data = libica.openapi.v3.models.data.Data(
                    id = '0', 
                    urn = '0', 
                    details = libica.openapi.v3.models.data_details.DataDetails(
                        time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        creator_id = '', 
                        tenant_id = '', 
                        tenant_name = '', 
                        owning_project_id = '', 
                        owning_project_name = '', 
                        name = '', 
                        path = '', 
                        file_size_in_bytes = 56, 
                        status = 'PARTIAL', 
                        tags = libica.openapi.v3.models.data_tag.DataTag(
                            technical_tags = [
                                ''
                                ], 
                            user_tags = [
                                ''
                                ], 
                            connector_tags = [
                                ''
                                ], 
                            run_in_tags = [
                                ''
                                ], 
                            run_out_tags = [
                                ''
                                ], 
                            reference_tags = [
                                ''
                                ], ), 
                        format = libica.openapi.v3.models.data_format.DataFormat(
                            id = '', 
                            time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            owner_id = '', 
                            tenant_id = '', 
                            tenant_name = '', 
                            code = '0', 
                            description = '0', 
                            mime_type = '0', ), 
                        data_type = 'FILE', 
                        object_e_tag = '', 
                        stored_for_the_first_time_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        region = libica.openapi.v3.models.region.Region(
                            id = '', 
                            time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            owner_id = '', 
                            tenant_id = '', 
                            tenant_name = '', 
                            code = '0', 
                            country = libica.openapi.v3.models.country.Country(
                                id = '', 
                                time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                owner_id = '', 
                                tenant_id = '', 
                                tenant_name = '', 
                                code = '', 
                                name = '', 
                                region = '', ), 
                            city_name = '0', ), 
                        application = libica.openapi.v3.models.application_v4.ApplicationV4(
                            id = '', 
                            name = '', ), 
                        will_be_archived_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        will_be_deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        sequencing_run = libica.openapi.v3.models.sequencing_run.SequencingRun(
                            id = '', 
                            instrument_run_id = '', 
                            name = '', ), ), 
                    folder_details = libica.openapi.v3.models.folder_details.FolderDetails(
                        non_indexed = True, ), )
            )
        else:
            return DataTransfer(
                id = '',
                time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                owner_id = '',
                tenant_id = '',
                reference = '0',
                direction = 'UPLOAD',
                data_transferred = 0,
                status = 'REQUESTED',
                data = libica.openapi.v3.models.data.Data(
                    id = '0', 
                    urn = '0', 
                    details = libica.openapi.v3.models.data_details.DataDetails(
                        time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        creator_id = '', 
                        tenant_id = '', 
                        tenant_name = '', 
                        owning_project_id = '', 
                        owning_project_name = '', 
                        name = '', 
                        path = '', 
                        file_size_in_bytes = 56, 
                        status = 'PARTIAL', 
                        tags = libica.openapi.v3.models.data_tag.DataTag(
                            technical_tags = [
                                ''
                                ], 
                            user_tags = [
                                ''
                                ], 
                            connector_tags = [
                                ''
                                ], 
                            run_in_tags = [
                                ''
                                ], 
                            run_out_tags = [
                                ''
                                ], 
                            reference_tags = [
                                ''
                                ], ), 
                        format = libica.openapi.v3.models.data_format.DataFormat(
                            id = '', 
                            time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            owner_id = '', 
                            tenant_id = '', 
                            tenant_name = '', 
                            code = '0', 
                            description = '0', 
                            mime_type = '0', ), 
                        data_type = 'FILE', 
                        object_e_tag = '', 
                        stored_for_the_first_time_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        region = libica.openapi.v3.models.region.Region(
                            id = '', 
                            time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            owner_id = '', 
                            tenant_id = '', 
                            tenant_name = '', 
                            code = '0', 
                            country = libica.openapi.v3.models.country.Country(
                                id = '', 
                                time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                owner_id = '', 
                                tenant_id = '', 
                                tenant_name = '', 
                                code = '', 
                                name = '', 
                                region = '', ), 
                            city_name = '0', ), 
                        application = libica.openapi.v3.models.application_v4.ApplicationV4(
                            id = '', 
                            name = '', ), 
                        will_be_archived_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        will_be_deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        sequencing_run = libica.openapi.v3.models.sequencing_run.SequencingRun(
                            id = '', 
                            instrument_run_id = '', 
                            name = '', ), ), 
                    folder_details = libica.openapi.v3.models.folder_details.FolderDetails(
                        non_indexed = True, ), ),
        )
        """

    def testDataTransfer(self):
        """Test DataTransfer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
