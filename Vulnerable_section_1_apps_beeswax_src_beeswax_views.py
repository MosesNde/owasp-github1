 from django.core.urlresolvers import reverse
 
 from desktop.appmanager import get_apps_dict
 from desktop.context_processors import get_app_name
 from desktop.lib.paginator import Paginator
 from desktop.lib.django_util import JsonResponse
         handle, state = _get_query_handle_and_state(query_history)
 
       if 'on_success_url' in request.GET:
        if request.GET.get('on_success_url'):
           action = 'watch-redirect'
         else:
           action = 'watch-results'