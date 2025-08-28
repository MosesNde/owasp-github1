 """ test for app action functionality """
from io import BytesIO
 from unittest.mock import patch
 import pathlib
 
from PIL import Image
from django.core.files.base import ContentFile
 from django.http import Http404
 from django.template.response import TemplateResponse
 from django.test import TestCase
         """there are so many views, this just makes sure it LOADS"""
         view = views.Status.as_view()
 
        image_file = pathlib.Path(__file__).parent.joinpath(
             "../../static/images/default_avi.jpg"
         )
        image = Image.open(image_file)
        output = BytesIO()
        image.save(output, format=image.format)
         with patch("bookwyrm.models.activitypub_mixin.broadcast_task.apply_async"):
             status = models.Review.objects.create(
                 content="hi",
             attachment = models.Image.objects.create(
                 status=status, caption="alt text here"
             )
            attachment.image.save("test.jpg", ContentFile(output.getvalue()))
 
         request = self.factory.get("")
         request.user = self.local_user