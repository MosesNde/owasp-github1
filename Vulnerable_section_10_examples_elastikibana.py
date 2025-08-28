 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
 
from libnmap.parser import NmapParser
from elasticsearch import Elasticsearch
 from datetime import datetime
 import pygeoip
 
 
 def store_report(nmap_report, database, index):
         cpelist = nmap_host.os.os_cpelist()
         if len(cpelist):
             mcpe = cpelist.pop()
            rval.update({
                    "vendor": mcpe.get_vendor(),
                    "product": mcpe.get_product()
            })
     return rval
 
 