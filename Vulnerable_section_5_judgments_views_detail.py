 from caselawclient.errors import JudgmentNotFoundError
 from caselawclient.models.judgments import Judgment
 from django.conf import settings
from django.http import Http404, HttpResponse
 from django.shortcuts import redirect
 from django.template.defaultfilters import filesizeformat
 from django.template.response import TemplateResponse
 
 def detail(request, judgment_uri):
     judgment = get_published_judgment_by_uri(judgment_uri)
     context = {}
 
     context["judgment"] = judgment.content_as_html("")  # "" is most recent version