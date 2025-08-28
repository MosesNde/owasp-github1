 #!/usr/bin/env python
 
 from libnmap.parser import NmapParser
from libnmap.reportjson import ReportDecoder
 from libnmap.plugins.es import NmapElasticsearchPlugin
from datetime import datetime
import json
 
 nmap_report = NmapParser.parse_fromfile("libnmap/test/files/1_hosts.xml")
 mindex = datetime.fromtimestamp(nmap_report.started).strftime("%Y-%m-%d")