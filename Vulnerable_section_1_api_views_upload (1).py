 from chunked_upload.models import ChunkedUpload
 from chunked_upload.views import ChunkedUploadCompleteView, ChunkedUploadView
 from constance import config as site_config
 from django.core.files.base import ContentFile
 from django.http import HttpResponseForbidden
 from django.shortcuts import get_object_or_404
 
     def on_completion(self, uploaded_file, request):
         user = User.objects.filter(id=request.POST.get("user")).first()
        # To-Do: Sanatize file name
        filename = request.POST.get("filename")
 
         # To-Do: Get origin device
         device = "web"