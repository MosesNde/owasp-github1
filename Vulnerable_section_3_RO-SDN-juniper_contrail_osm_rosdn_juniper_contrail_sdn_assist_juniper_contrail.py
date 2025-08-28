         self.fabric = None
         overlay_url = None
         self.vni_range = None
 
         if config:
             auth_url = config.get("auth_url")
             self.overlay_url = config.get("overlay_url")
             self.vni_range = config.get("vni_range")
 
         if not url:
             raise SdnConnectorError("'url' must be provided")
 
             "domain": self.domain,
             "asn": self.asn,
             "fabric": self.fabric,
         }
         self.underlay_api = UnderlayApi(
             url,