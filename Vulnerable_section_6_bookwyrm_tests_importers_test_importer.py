     return datetime.datetime(*args, tzinfo=pytz.UTC)
 
 
# pylint: disable=consider-using-with
 @patch("bookwyrm.suggested_users.rerank_suggestions_task.delay")
 @patch("bookwyrm.activitystreams.populate_stream_task.delay")
 @patch("bookwyrm.activitystreams.add_book_statuses_task.delay")
         """use a test csv"""
         self.importer = Importer()
         datafile = pathlib.Path(__file__).parent.joinpath("../data/generic.csv")
         self.csv = open(datafile, "r", encoding=self.importer.encoding)
 
     @classmethod
     def setUpTestData(cls):
         """populate database"""