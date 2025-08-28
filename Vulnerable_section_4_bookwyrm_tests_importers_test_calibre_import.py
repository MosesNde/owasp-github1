 from bookwyrm.models.import_job import handle_imported_book
 
 
# pylint: disable=consider-using-with
 @patch("bookwyrm.suggested_users.rerank_suggestions_task.delay")
 @patch("bookwyrm.activitystreams.populate_stream_task.delay")
 @patch("bookwyrm.activitystreams.add_book_statuses_task.delay")
         """use a test csv"""
         self.importer = CalibreImporter()
         datafile = pathlib.Path(__file__).parent.joinpath("../data/calibre.csv")
         self.csv = open(datafile, "r", encoding=self.importer.encoding)
 
     @classmethod
     def setUpTestData(cls):
         """populate database"""