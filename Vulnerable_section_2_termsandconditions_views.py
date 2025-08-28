 from django.utils.translation import gettext as _
 from django.views.generic import DetailView, CreateView, FormView
 from django.template.loader import get_template
 import logging
 from smtplib import SMTPException
 
             terms = TermsAndConditions.get_active_terms_not_agreed_to(self.request.user)
         return terms
 
 
 class AcceptTermsView(CreateView, GetTermsViewMixin):
     """
         LOGGER.debug("termsandconditions.views.AcceptTermsView.get_initial")
 
         terms = self.get_terms(self.kwargs)
        return_to = self.request.GET.get("returnTo", "/")
 
         return {"terms": terms, "returnTo": return_to}
 
     def post(self, request, *args, **kwargs):
         """
         Handles POST request.
         """
        return_url = request.POST.get("returnTo", "/")
         terms_ids = request.POST.getlist("terms")
 
        parsed = urlparse(return_url)
        if parsed.hostname and parsed.hostname not in settings.ALLOWED_HOSTS:
            # Make sure the return url is a relative path or a trusted hostname
            return_url = '/'

         if not terms_ids:  # pragma: nocover
             return HttpResponseRedirect(return_url)
 
 
         terms = self.get_terms(self.kwargs)
 
        return_to = self.request.GET.get("returnTo", "/")
 
         return {"terms": terms, "returnTo": return_to}
 
                 _("An Error Occurred Sending Your Message."),
             )
 
        self.success_url = form.cleaned_data.get("returnTo", "/") or "/"
 
         return super().form_valid(form)
 