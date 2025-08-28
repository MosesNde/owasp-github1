 
 # pylint: disable=unused-argument
 # pylint: disable=missing-function-docstring
# pylint: disable=consider-using-with
 class PreviewImages(TestCase):
     """every response to a get request, html or json"""
 
     def setUp(self):
         """we need basic test data and mocks"""
         self.factory = RequestFactory()
        avatar_file = pathlib.Path(__file__).parent.joinpath(
             "../static/images/no_cover.jpg"
         )
         with (
             patch("bookwyrm.suggested_users.rerank_suggestions_task.delay"),
             patch("bookwyrm.activitystreams.populate_stream_task.delay"),
             patch("bookwyrm.lists_stream.populate_lists_task.delay"),
         ):
             self.local_user = models.User.objects.create_user(
                 "possum@local.com",
                 local=True,
                 localname="possum",
                 avatar=SimpleUploadedFile(
                    avatar_file,
                    open(avatar_file, "rb").read(),
                     content_type="image/jpeg",
                 ),
             )
             patch("bookwyrm.suggested_users.rerank_suggestions_task.delay"),
             patch("bookwyrm.activitystreams.populate_stream_task.delay"),
             patch("bookwyrm.lists_stream.populate_lists_task.delay"),
         ):
             self.remote_user_with_preview = models.User.objects.create_user(
                 "badger@your.domain.here",
                 inbox="https://example.com/users/badger/inbox",
                 outbox="https://example.com/users/badger/outbox",
                 avatar=SimpleUploadedFile(
                    avatar_file,
                    open(avatar_file, "rb").read(),
                     content_type="image/jpeg",
                 ),
             )
         settings.ENABLE_PREVIEW_IMAGES = True
 
     def test_generate_preview_image(self, *args, **kwargs):
        image_file = pathlib.Path(__file__).parent.joinpath(
             "../static/images/no_cover.jpg"
         )
 
             "text_three": "@possum@local.com",
         }
 
        result = generate_preview_image(texts=texts, picture=image_file, rating=5)
         self.assertIsInstance(result, Image.Image)
         self.assertEqual(
             result.size, (settings.PREVIEW_IMG_WIDTH, settings.PREVIEW_IMG_HEIGHT)