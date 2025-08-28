 from c2cgeoportal_commons.lib.email_ import send_email_config
 from c2cgeoportal_commons.models import DBSession
 from c2cgeoportal_commons.models.static import Shorturl
 from c2cgeoportal_geoportal.lib.common_headers import Cache, set_common_headers
 
 logger = logging.getLogger(__name__)
         if len(url) > 8190:
             raise HTTPBadRequest(f"The parameter url is too long ({len(url)} > {8190})")
 
        # Check that it is an internal URL...
        uri_parts = urlparse(url)
        if "allowed_hosts" in self.settings:
            if uri_parts.netloc not in self.settings["allowed_hosts"]:
                raise HTTPBadRequest(
                    f"The requested host '{uri_parts.netloc}' is not part of allowed hosts: "
                    f"{', '.join(self.settings['allowed_hosts'])}"
                )
        else:
            hostname = uri_parts.hostname
            if hostname != self.request.server_name:
                raise HTTPBadRequest(
                    f"The requested host '{hostname!s}' should be '{self.request.server_name!s}'"
                )
 
         shortened = False
 
         for base in self.short_bases:
             base_parts = urlparse(base)
             if uri_parts.path.startswith(base_parts.path):