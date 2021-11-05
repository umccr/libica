from libica.app import GDSFilesEventType
from tests.app import IcaUnitTests, IcaIntegrationTests, logger


class InitUnitTests(IcaUnitTests):

    def test_gds_files_event_type(self):
        """
        python -m unittest tests.app.test_ica.InitUnitTests.test_gds_files_event_type
        """
        event_type = GDSFilesEventType.from_value("deleted")
        self.assertEqual(event_type, GDSFilesEventType.DELETED)

        event_type = GDSFilesEventType.from_value("uploaded")
        self.assertEqual(event_type, GDSFilesEventType.UPLOADED)

        event_type = GDSFilesEventType.from_value("archived")
        self.assertEqual(event_type, GDSFilesEventType.ARCHIVED)

        event_type = GDSFilesEventType.from_value("unarchived")
        self.assertEqual(event_type, GDSFilesEventType.UNARCHIVED)

        try:
            _ = GDSFilesEventType.from_value("unknown")
        except Exception as e:
            logger.exception(f"THIS ERROR EXCEPTION IS INTENTIONAL FOR TEST. NOT ACTUAL ERROR. \n{e}")
        self.assertRaises(ValueError)


class InitIntegrationTests(IcaIntegrationTests):
    pass
