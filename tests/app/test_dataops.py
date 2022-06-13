from libica.app import dataops

from tests.app import IcaUnitTests, IcaIntegrationTests, logger

mock_abs_uri_1 = (
    "BSSH clinical-genomics-workgroup",
    "/test_folder/pd_dragen_germline_test4-DRAGEN Germline Whole Genome 3-10-4-76766071-2bb0-46c3-abba-b393851caa60/NA12878-PCRF450-1_S1/dragen_run_1651468354177_3033.log",
    "icav2://BSSH+clinical-genomics-workgroup/test_folder/pd_dragen_germline_test4-DRAGEN+Germline+Whole+Genome+3-10-4-76766071-2bb0-46c3-abba-b393851caa60/NA12878-PCRF450-1_S1/dragen_run_1651468354177_3033.log",
)

mock_abs_uri_2 = (
    "playground_v2",
    "/test_folder/foo1.txt",
    "icav2://playground_v2/test_folder/foo1.txt",
)

mock_abs_uri_3 = (
    "playground_v2",
    "/pd_dragen_germline_test3-DRAGEN_germline_393-078e4127-c3a7-4aa4-a0cb-0170c034c9e4/",
    "icav2://playground_v2/pd_dragen_germline_test3-DRAGEN_germline_393-078e4127-c3a7-4aa4-a0cb-0170c034c9e4/",
)


class DataOpsUnitTests(IcaUnitTests):

    def test_to_uri(self):
        """
        python -m unittest tests.app.test_dataops.DataOpsUnitTests.test_to_uri
        """
        abs_uri = dataops.to_uri(
            project_name=mock_abs_uri_1[0],
            file_path=mock_abs_uri_1[1]
        )
        logger.info(abs_uri)
        self.assertEqual(abs_uri, mock_abs_uri_1[2])

        abs_uri = dataops.to_uri(
            project_name=mock_abs_uri_2[0],
            file_path=mock_abs_uri_2[1]
        )
        logger.info(abs_uri)
        self.assertEqual(abs_uri, mock_abs_uri_2[2])

        abs_uri = dataops.to_uri(
            project_name=mock_abs_uri_3[0],
            file_path=mock_abs_uri_3[1]
        )
        logger.info(abs_uri)
        self.assertEqual(abs_uri, mock_abs_uri_3[2])

    def test_from_uri(self):
        """
        python -m unittest tests.app.test_dataops.DataOpsUnitTests.test_from_uri
        """
        project_name, path_ = dataops.from_uri(mock_abs_uri_1[2])
        logger.info((project_name, path_))
        self.assertEqual(mock_abs_uri_1[0], project_name)

        logger.info(dataops.from_uri(mock_abs_uri_2[2]))
        logger.info(dataops.from_uri(mock_abs_uri_3[2]))


class DataOpsIntegrationTests(IcaIntegrationTests):
    pass
