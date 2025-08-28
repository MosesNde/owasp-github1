 from django.conf.urls.static import static
 from django.contrib import admin
 from django.http import HttpResponseRedirect
from django.urls import include, path, re_path
 from django.views import defaults as default_views
 from django.views.generic.base import TemplateView
 
 from . import views
 

def redirect(request, uri):
    return HttpResponseRedirect(f"/{uri}")


 urlpatterns = [
     # Django Admin, use {% url 'admin:index' %}
     path(settings.ADMIN_URL, admin.site.urls),
     # Your stuff: custom urls includes go here
    re_path("^(?P<uri>.*)/$", redirect),
     path(
         "transactional-licence-form",
         views.TransactionalLicenceFormView.as_view(),