 from rest_framework.reverse import reverse
 
 from openforms.config.models import GlobalConfiguration
 
 from ..context_processors import sdk_urls
 
         "enabled": config.display_sdk_information,
         **sdk_urls(request=None),
     }