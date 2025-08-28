 
 from copy import deepcopy
 import logging
from random import randrange
 from uuid import uuid4
 
 from osm_ro_plugin import vimconn
             if iface.get("type") in ("SR-IOV", "PCI-PASSTHROUGH") and self.config.get(
                 "sdn-port-mapping"
             ):
                compute_index = randrange(len(self.config["sdn-port-mapping"]))
                port_index = randrange(
                     len(self.config["sdn-port-mapping"][compute_index]["ports"])
                 )
                 interface["compute_node"] = self.config["sdn-port-mapping"][