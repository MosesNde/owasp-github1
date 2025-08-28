 """ testing models """
from io import BytesIO
 from collections import namedtuple
 from dataclasses import dataclass
 import datetime
 from unittest import expectedFailure
 from unittest.mock import patch
 
from PIL import Image
 import responses
 
 from django.core.exceptions import ValidationError
         user = User.objects.create_user(
             "mouse", "mouse@mouse.mouse", "mouseword", local=True, localname="mouse"
         )
        image_file = pathlib.Path(__file__).parent.joinpath(
             "../../static/images/default_avi.jpg"
         )
        image = Image.open(image_file)
        output = BytesIO()
        image.save(output, format=image.format)
        user.avatar.save("test.jpg", ContentFile(output.getvalue()))
 
         instance = fields.ImageField()
 
     @responses.activate
     def test_image_field_set_field_from_activity_no_overwrite_with_cover(self, *_):
         """update a model instance from an activitypub object"""
        image_file = pathlib.Path(__file__).parent.joinpath(
             "../../static/images/default_avi.jpg"
         )
        image = Image.open(image_file)
        output = BytesIO()
        image.save(output, format=image.format)

        another_image_file = pathlib.Path(__file__).parent.joinpath(
             "../../static/images/logo.png"
         )
        another_image = Image.open(another_image_file)
        another_output = BytesIO()
        another_image.save(another_output, format=another_image.format)
 
         instance = fields.ImageField(activitypub_field="cover", name="cover")
 
        responses.add(
            responses.GET,
            "http://www.example.com/image.jpg",
            body=another_image.tobytes(),
            status=200,
        )
         book = Edition.objects.create(title="hello")
        book.cover.save("test.jpg", ContentFile(output.getvalue()))
         cover_size = book.cover.size
         self.assertIsNotNone(cover_size)
 
     @responses.activate
     def test_image_field_set_field_from_activity_with_overwrite_with_cover(self, *_):
         """update a model instance from an activitypub object"""
        image_file = pathlib.Path(__file__).parent.joinpath(
             "../../static/images/default_avi.jpg"
         )
        image = Image.open(image_file)
        output = BytesIO()
        image.save(output, format=image.format)
         book = Edition.objects.create(title="hello")
        book.cover.save("test.jpg", ContentFile(output.getvalue()))
         cover_size = book.cover.size
         self.assertIsNotNone(cover_size)
 
        another_image_file = pathlib.Path(__file__).parent.joinpath(
             "../../static/images/logo.png"
         )
 
         instance = fields.ImageField(activitypub_field="cover", name="cover")
 
        with open(another_image_file, "rb") as another_image:
             responses.add(
                 responses.GET,
                 "http://www.example.com/image.jpg",