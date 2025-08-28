 from django import forms
 from django import http
 from django import shortcuts
 from django.views import generic
 
 from horizon import exceptions
         workflow = self.get_workflow()
         workflow.verify_integrity()
         context[self.context_object_name] = workflow
        next = self.request.GET.get(workflow.redirect_param_name)
        context['REDIRECT_URL'] = next
         context['layout'] = self.get_layout()
         # For consistency with Workflow class
         context['modal'] = 'modal' in context['layout']