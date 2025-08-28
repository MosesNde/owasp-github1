     return datetime.datetime(*args, tzinfo=pytz.UTC)
 
 
# pylint: disable=consider-using-with
 @patch("bookwyrm.suggested_users.rerank_suggestions_task.delay")
 @patch("bookwyrm.activitystreams.populate_stream_task.delay")
 @patch("bookwyrm.activitystreams.add_book_statuses_task.delay")
         datafile = pathlib.Path(__file__).parent.joinpath("../data/librarything.tsv")
 
         # Librarything generates latin encoded exports...
         self.csv = open(datafile, "r", encoding=self.importer.encoding)
 
     @classmethod
     def setUpTestData(cls):
         """populate database"""