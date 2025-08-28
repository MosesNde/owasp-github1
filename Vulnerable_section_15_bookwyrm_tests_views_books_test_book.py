 """ test for app action functionality """
from io import BytesIO
 import pathlib
 from unittest.mock import patch
from PIL import Image
 
 import responses
 
     def test_upload_cover_file(self):
         """add a cover via file upload"""
         self.assertFalse(self.book.cover)
        image_file = pathlib.Path(__file__).parent.joinpath(
             "../../../static/images/default_avi.jpg"
         )
 
         form = forms.CoverForm(instance=self.book)
        # pylint: disable=consider-using-with
        form.data["cover"] = SimpleUploadedFile(
            image_file, open(image_file, "rb").read(), content_type="image/jpeg"
        )
 
         request = self.factory.post("", form.data)
         request.user = self.local_user
 def _setup_cover_url():
     """creates cover url mock"""
     cover_url = "http://example.com"
    image_file = pathlib.Path(__file__).parent.joinpath(
         "../../../static/images/default_avi.jpg"
     )
    image = Image.open(image_file)
    output = BytesIO()
    image.save(output, format=image.format)
    responses.add(
        responses.GET,
        cover_url,
        body=output.getvalue(),
        status=200,
    )
     return cover_url