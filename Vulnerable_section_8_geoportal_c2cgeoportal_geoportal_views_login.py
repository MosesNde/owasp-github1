 from c2cgeoportal_commons import models
 from c2cgeoportal_commons.lib.email_ import send_email_config
 from c2cgeoportal_commons.models import static
from c2cgeoportal_geoportal import is_valid_referrer
 from c2cgeoportal_geoportal.lib import get_setting, is_intranet, oauth2
 from c2cgeoportal_geoportal.lib.caching import get_region
 from c2cgeoportal_geoportal.lib.common_headers import Cache, set_common_headers
                 self._oauth2_login(user)
 
             headers = remember(self.request, username)
             came_from = self.request.params.get("came_from")
             if came_from:
                 return HTTPFound(location=came_from, headers=headers)
             headers.append(("Content-Type", "text/json"))
             return set_common_headers(
                 self.request,
             self.request.tm.commit()
         LOG.debug("OAuth create_authorization_response return\nstatus: %s\nbody:\n%s", status, body)
 
         if status == 302:
            raise HTTPFound(location=headers["Location"])
         if status != 200:
             if body:
                 raise exception_response(status, details=body)