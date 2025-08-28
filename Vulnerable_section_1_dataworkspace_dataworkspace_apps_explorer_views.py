 from django.contrib.auth.views import LoginView
 from django.contrib import messages
 from django.db.models import Count
 from django.http import (
     Http404,
     HttpResponse,
             return HttpResponseRedirect(self.get_edit_sql_url(request, query))
 
         else:
            return HttpResponseBadRequest(f"Unknown form action: {action}")
 
     @staticmethod
     def get_edit_sql_url(request, query):