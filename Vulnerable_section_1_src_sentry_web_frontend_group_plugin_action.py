 
 from django.http import Http404, HttpResponseRedirect
 from django.shortcuts import get_object_or_404
 
 from sentry.models import Group, GroupMeta
 from sentry.plugins import plugins
         if response:
             return response
 
        redirect = request.META.get('HTTP_REFERER') or '/{}/{}/'.format(
            organization.slug,
            group.project.slug,
        )
         return HttpResponseRedirect(redirect)