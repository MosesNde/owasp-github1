 from django.shortcuts import redirect, render
 from django.urls import reverse
 from django.utils.decorators import method_decorator
 from django.utils.text import slugify
 from django.utils.translation import get_language_from_request
 from django.utils.translation import gettext as _
 )
 
 
 def verify_edx_resources():
     """
     Ensure that all necessary resources to render the view are present.
 
         context_data = get_global_context(request, enterprise_customer)
 
         if not (success_url and failure_url):
             return render_page_with_error_code_message(
                 request, context_data, REDIRECT_URLS_MISSING_ERROR_CODE,
         )
         initial.update({
             'enterprises': [(str(uuid), name) for uuid, name in enterprises],
            'success_url': self.request.GET.get('success_url'),
             'user_id': self.request.user.id
         })
         LOGGER.info(