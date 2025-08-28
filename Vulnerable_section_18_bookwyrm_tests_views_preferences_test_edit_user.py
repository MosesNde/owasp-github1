         form.data["email"] = "wow@email.com"
         form.data["default_post_privacy"] = "public"
         form.data["preferred_timezone"] = "UTC"
        image_file = pathlib.Path(__file__).parent.joinpath(
             "../../../static/images/no_cover.jpg"
         )
        # pylint: disable=consider-using-with
        form.data["avatar"] = SimpleUploadedFile(
            image_file, open(image_file, "rb").read(), content_type="image/jpeg"
        )
         request = self.factory.post("", form.data)
         request.user = self.local_user
 
 
     def test_crop_avatar(self, _):
         """reduce that image size"""
        image_file = pathlib.Path(__file__).parent.joinpath(
             "../../../static/images/no_cover.jpg"
         )
        image = Image.open(image_file)
 
        result = views.preferences.edit_user.crop_avatar(image)
         self.assertIsInstance(result, ContentFile)
        image_result = Image.open(result)
        self.assertEqual(image_result.size, (120, 120))