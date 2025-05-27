import uuid
from contextlib import closing
from unittest import TestCase

from libica.openapi.v2 import Configuration, ApiClient
from libica.openapi.v2.api.project_analysis_api import ProjectAnalysisApi
from libica.openapi.v2.model.analysis_data_input import AnalysisDataInput
from libica.openapi.v2.model.analysis_output_mapping import AnalysisOutputMapping
from libica.openapi.v2.model.analysis_parameter_input import AnalysisParameterInput
from libica.openapi.v2.model.create_analysis_tag import CreateAnalysisTag
from libica.openapi.v2.model.analysis_v3 import AnalysisV3
from libica.openapi.v2.model.analysis_v4 import AnalysisV4
from libica.openapi.v2.model.create_nextflow_analysis import CreateNextflowAnalysis
from libica.openapi.v2.model.nextflow_analysis_input import NextflowAnalysisInput
from tests import MOCK_EP

project_id = str(uuid.uuid4())

nextflow_analysis = CreateNextflowAnalysis(
    user_reference='PTC-ctTSO-v2-launch-test-mock',
    pipeline_id=str(uuid.uuid4()),
    tags=CreateAnalysisTag(
        reference_tags=[],
        technical_tags=[
            'portal_run_id=20240308abcd6789'
        ],
        user_tags=[
            'subject_id=SBJ04405',
            'library_id=L2301368',
            'instrument_run_id=231116_A01052_0172_BHVLM5DSX7',  # pragma: allowlist secret
            'project_owner=UMCCR',
            'project_name=testing'
        ]
    ),
    analysis_input=NextflowAnalysisInput(
        inputs=[
            AnalysisDataInput(
                data_ids=['fol.11122333edd141213e0f08dc3cace45e'],
                parameter_code='run_folder'
            ),
            AnalysisDataInput(
                data_ids=['fil.888888f5b9e94977b0a308dc388cf24f'],
                parameter_code='sample_sheet'
            ),
        ],
        parameters=[
            AnalysisParameterInput(
                code="StartsFromFastq",
                value="true",
            ),
            AnalysisParameterInput(
                code="sample_pair_ids",
                multi_value=["L2301368"]
            )
        ],
        activation_code_detail_id=str(uuid.uuid4()),
        analysis_storage_id=str(uuid.uuid4()),
        analysis_output=[
            AnalysisOutputMapping(
                source_path='out/',
                target_path='/ilmn_cttso_fastq_cache/20240308abcd6789/',
                target_project_id=project_id,
                type='FOLDER'
            )
        ]
    )
)


class Issue135IntegrationTests(TestCase):
    """
    Dedicated test cases for request and response type version switching from API endpoint.
    See https://github.com/umccr/libica/issues/135

    How to run these tests:
    1. `make up` from the project root to spin up ICAv2 mock endpoints (see README)
    2. copy and run the command from each test case pydoc string
    """

    def setUp(self) -> None:
        super(Issue135IntegrationTests, self).setUp()

        icav2_access_token = "MOCK"
        ica_url = MOCK_EP

        self.configuration = Configuration(
            host=ica_url,
            access_token=icav2_access_token,
        )
        self.configuration.debug = True  # debug all API calls

        with closing(ApiClient(self.configuration)) as _c:
            self.api_client: ApiClient = _c

    def tearDown(self) -> None:
        self.api_client.pool.close()

    def test_create_nextflow_analysis(self):
        """
        python -m unittest tests.v2.test_issue_135.Issue135IntegrationTests.test_create_nextflow_analysis
        """

        # implicit, by default SDK client assume the latest version i.e. V4

        api_instance = ProjectAnalysisApi(self.api_client)

        api_response: AnalysisV4 = api_instance.create_nextflow_analysis(
            project_id,
            nextflow_analysis,
        )

        print("-" * 128)

        print(type(api_response))
        # print(dir(api_response))
        self.assertIsNotNone(api_response)

        # assert that api response object is of type V4
        self.assertIsInstance(api_response, AnalysisV4)

        # assert that tenant is nested object having "id" property
        api_response_d = api_response.to_dict()
        tenant = api_response_d.get("tenant")
        self.assertIn("id", tenant.keys())
        print(tenant)

    def test_create_nextflow_analysis_with_v4(self):
        """
        python -m unittest tests.v2.test_issue_135.Issue135IntegrationTests.test_create_nextflow_analysis_with_v4
        """

        # set explicitly the request media type and header versioning to V4
        self.api_client.set_default_header(
            header_name="Content-Type",
            header_value="application/vnd.illumina.v4+json",
        )
        self.api_client.set_default_header(
            header_name="Accept",
            header_value="application/vnd.illumina.v4+json",
        )

        api_instance = ProjectAnalysisApi(self.api_client)

        # NOTE: the AnalysisV4 is the default response_type in settings by SDK generator

        # override endpoint settings response type to the version we want i.e. AnalysisV4
        endpoint_settings = api_instance.create_nextflow_analysis_endpoint.settings
        endpoint_settings['response_type'] = (AnalysisV4,)

        api_response = api_instance.create_nextflow_analysis(
            project_id,
            nextflow_analysis,
        )

        print("-" * 128)

        # assert request client headers
        self.assertEqual(self.api_client.default_headers['Content-Type'], "application/vnd.illumina.v4+json")
        self.assertEqual(self.api_client.default_headers['Accept'], "application/vnd.illumina.v4+json")
        print(self.api_client.default_headers)

        print(type(api_response))
        # print(dir(api_response))
        self.assertIsNotNone(api_response)
        self.assertIsInstance(api_response, AnalysisV4)

        # assert these keys exist in response body
        print(api_response['owner'])
        print(api_response['tenant'])

    def test_create_nextflow_analysis_with_v3(self):
        """
        python -m unittest tests.v2.test_issue_135.Issue135IntegrationTests.test_create_nextflow_analysis_with_v3
        """

        # set explicitly the request media type and header versioning to V3
        self.api_client.set_default_header(
            header_name="Content-Type",
            header_value="application/vnd.illumina.v3+json",
        )
        self.api_client.set_default_header(
            header_name="Accept",
            header_value="application/vnd.illumina.v3+json",
        )

        api_instance = ProjectAnalysisApi(self.api_client)

        # override endpoint settings response type to the version we want i.e. AnalysisV3 or Analysis
        endpoint_settings = api_instance.create_nextflow_analysis_endpoint.settings
        endpoint_settings['response_type'] = (AnalysisV3,)

        api_response = api_instance.create_nextflow_analysis(
            project_id,
            nextflow_analysis,
        )

        print("-" * 128)

        # assert request client headers
        self.assertEqual(self.api_client.default_headers['Content-Type'], "application/vnd.illumina.v3+json")
        self.assertEqual(self.api_client.default_headers['Accept'], "application/vnd.illumina.v3+json")
        print(self.api_client.default_headers)

        # assert response type V3
        print(type(api_response))
        # print(dir(api_response))
        self.assertIsNotNone(api_response)
        self.assertIsInstance(api_response, AnalysisV3)

        # assert these keys exist in response body
        print("owner_id:", api_response['owner_id'])
        print("tenant_id:", api_response['tenant_id'])
