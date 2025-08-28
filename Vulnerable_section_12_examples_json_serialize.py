 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
 
 from libnmap.parser import NmapParser
 from libnmap.reportjson import ReportDecoder, ReportEncoder
import json
 
 nmap_report_obj = NmapParser.parse_fromfile("libnmap/test/files/1_hosts.xml")
 