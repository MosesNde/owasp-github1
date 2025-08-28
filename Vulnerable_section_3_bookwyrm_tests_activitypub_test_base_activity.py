 """ tests the base functionality for activitypub dataclasses """
from io import BytesIO
 import json
 import pathlib
 from unittest.mock import patch
 
 from dataclasses import dataclass
 from django.test import TestCase
from PIL import Image
 import responses
 
 from bookwyrm import activitypub
         # don't try to load the user icon
         del self.userdata["icon"]
 
        image_file = pathlib.Path(__file__).parent.joinpath(
             "../../static/images/default_avi.jpg"
         )
        image = Image.open(image_file)
        output = BytesIO()
        image.save(output, format=image.format)
        self.image_data = output.getvalue()
 
     def test_get_representative_not_existing(self, *_):
         """test that an instance representative actor is created if it does not exist"""