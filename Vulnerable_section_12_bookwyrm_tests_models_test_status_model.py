 """ testing models """
 from unittest.mock import patch
from io import BytesIO
 import pathlib
 import re
 
 from django.http import Http404
from django.core.files.base import ContentFile
 from django.db import IntegrityError
 from django.contrib.auth.models import AnonymousUser
 from django.test import TestCase
 from django.utils import timezone
from PIL import Image
 import responses
 
 from bookwyrm import activitypub, models, settings
         """individual test setup"""
         self.anonymous_user = AnonymousUser
         self.anonymous_user.is_authenticated = False
        image_file = pathlib.Path(__file__).parent.joinpath(
             "../../static/images/default_avi.jpg"
         )
        image = Image.open(image_file)
        output = BytesIO()
        with patch("bookwyrm.models.Status.broadcast"):
            image.save(output, format=image.format)
            self.book.cover.save("test.jpg", ContentFile(output.getvalue()))
 
     def test_status_generated_fields(self, *_):
         """setting remote id"""