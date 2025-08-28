 from io import StringIO
 
 from django.core.management import call_command
from django.test import override_settings
 from django.urls import reverse
 
 from cookie_consent.cache import delete_cache
 from cookie_consent.models import CookieGroup
 from django_webtest import WebTest
 
 from openforms.config.models import GlobalConfiguration
 from openforms.forms.tests.factories import FormFactory
             self.assertTemplateUsed(
                 refreshed_form_page, "includes/analytics/all_bottom.html"
             )