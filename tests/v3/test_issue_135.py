import uuid
from unittest import TestCase

from libica.openapi.v3 import Configuration, ApiClient, ProjectAnalysisApi, CreateNextflowAnalysis, \
    NextflowAnalysisInput, CreateAnalysisTag, AnalysisDataInput, AnalysisParameterInput, AnalysisV4, AnalysisV3, \
    AnalysisReferenceDataParameter, AnalysisOutputMapping
from tests import MOCK_EP

project_id = str(uuid.uuid4())

nextflow_analysis = CreateNextflowAnalysis(
    userReference='PTC-ctTSO-v2-launch-test-mock',
    pipelineId=str(uuid.uuid4()),
    activationCodeDetailId=str(uuid.uuid4()),
    analysisStorageId=str(uuid.uuid4()),
    tags=CreateAnalysisTag(
        referenceTags=[],
        technicalTags=[
            'portal_run_id=20240308abcd6789'
        ],
        userTags=[
            'subject_id=SBJ04405',
            'library_id=L2301368',
            'instrument_run_id=231116_A01052_0172_BHVLM5DSX7',  # pragma: allowlist secret
            'project_owner=UMCCR',
            'project_name=testing'
        ]
    ),
    analysisInput=NextflowAnalysisInput(
        inputs=[
            AnalysisDataInput(
                dataIds=['fol.11122333edd141213e0f08dc3cace45e'],
                parameterCode='run_folder'
            ),
            AnalysisDataInput(
                dataIds=['fil.888888f5b9e94977b0a308dc388cf24f'],
                parameterCode='sample_sheet'
            ),
        ],
        parameters=[
            AnalysisParameterInput(
                code="StartsFromFastq",
                value="true",
            ),
            AnalysisParameterInput(
                code="sample_pair_ids",
                multiValue=["L2301368"]
            )
        ],
        referenceDataParameters=[
            AnalysisReferenceDataParameter(
                parameterCode="sample_pair_ids",
                referenceDataId=str(uuid.uuid4()),
            )
        ],
    ),
    analysisOutput=[
        AnalysisOutputMapping(
            sourcePath='out/',
            targetPath='/ilmn_cttso_fastq_cache/20240308abcd6789/',
            targetProjectId=project_id,
            type='FOLDER'
        )
    ]
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

        self.api_client: ApiClient = ApiClient(self.configuration)

    def tearDown(self) -> None:
        pass

    def test_create_nextflow_analysis(self):
        """
        python -m unittest tests.v3.test_issue_135.Issue135IntegrationTests.test_create_nextflow_analysis
        """

        # In v3 SDK, the SDK ApiClient set "Accept" header default to "application/vnd.illumina.v3+json"
        # See https://github.com/umccr/libica/issues/139
        self.api_client.set_default_header(
            header_name="Accept",
            header_value="application/vnd.illumina.v4+json",
        )

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
        python -m unittest tests.v3.test_issue_135.Issue135IntegrationTests.test_create_nextflow_analysis_with_v4
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

        api_response = api_instance.create_nextflow_analysis(
            project_id,
            nextflow_analysis,
        )

        print("-" * 128)

        # the AnalysisV4 is the default response_type in settings by SDK generator

        # assert request client headers
        self.assertEqual(self.api_client.default_headers['Content-Type'], "application/vnd.illumina.v4+json")
        self.assertEqual(self.api_client.default_headers['Accept'], "application/vnd.illumina.v4+json")
        print(self.api_client.default_headers)

        print(type(api_response))
        # print(dir(api_response))
        self.assertIsNotNone(api_response)
        self.assertIsInstance(api_response, AnalysisV4)

        # assert these keys exist in response body
        print(hasattr(api_response, 'owner'))
        print(hasattr(api_response, 'tenant'))

    def test_create_nextflow_analysis_with_v3(self):
        """
        python -m unittest tests.v3.test_issue_135.Issue135IntegrationTests.test_create_nextflow_analysis_with_v3
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

        api_instance: ProjectAnalysisApi = ProjectAnalysisApi(self.api_client)

        with self.assertRaises(Exception) as x:

            # FIXME In v3 SDK, as it has become supporting more "Static Typing", the generator tends to fix
            #  into one response type mapping. Unaware of "endpoint Header versioning and switching". Consequently
            #  this now "hard" map to return AnalysisV4 and, Pydantic will attempt to validate and fail.
            #  No easy workaround. Fallback to use v2 SDK in this case.
            #  Perhaps, the client should upgrade to AnalysisV4.

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
            print(dir(api_response))
            self.assertIsNotNone(api_response)
            self.assertIsInstance(api_response, AnalysisV3)

            # assert these keys exist in response body
            print("owner_id:", api_response['owner_id'])
            print("tenant_id:", api_response['tenant_id'])

        print("*" * 128)
        print(x.exception)
