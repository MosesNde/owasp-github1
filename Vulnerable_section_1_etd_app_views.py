 from django.core.urlresolvers import reverse
 from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseForbidden, JsonResponse, FileResponse, HttpResponseServerError
 from django.shortcuts import render, get_object_or_404
 from django.views.decorators.http import require_http_methods
 from .models import Person, Candidate, Keyword, CommitteeMember
 from .widgets import ID_VAL_SEPARATOR
 
 def login(request):
     if request.user.is_authenticated():
        next_url = request.GET.get('next', reverse('home'))
         return HttpResponseRedirect(next_url)
     else:
         logger.error('login() - got anonymous user: %s' % request.META)