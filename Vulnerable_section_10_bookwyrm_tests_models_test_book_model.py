 """ testing models """
from io import BytesIO
 import pathlib
 
 import pytest
 
 from dateutil.parser import parse
from PIL import Image
from django.core.files.base import ContentFile
 from django.test import TestCase
 from django.utils import timezone
 
     )
     def test_thumbnail_fields(self):
         """Just hit them"""
        image_file = pathlib.Path(__file__).parent.joinpath(
             "../../static/images/default_avi.jpg"
         )
        image = Image.open(image_file)
        output = BytesIO()
        image.save(output, format=image.format)
 
         book = models.Edition.objects.create(title="hello")
        book.cover.save("test.jpg", ContentFile(output.getvalue()))
 
         self.assertIsNotNone(book.cover_bw_book_xsmall_webp.url)
         self.assertIsNotNone(book.cover_bw_book_xsmall_jpg.url)