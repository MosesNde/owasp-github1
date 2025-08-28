 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
 
import unittest
 import os
 from libnmap.parser import NmapParser
 
 
         r1 = NmapParser.parse_fromfile("%s/%s" % (fdir, "files/1_hosts.xml"))
         r2 = NmapParser.parse_fromfile("%s/%s" % (fdir, "files/2_hosts.xml"))
         r3 = NmapParser.parse_fromfile("%s/%s" % (fdir, "files/1_hosts.xml"))
        r4 = NmapParser.parse_fromfile("%s/%s" % (fdir, "files/2_hosts_achange.xml"))
 
         d1 = r1.diff(r2)
         self.assertEqual(
             d1.changed(),
            set(["hosts_total", "commandline", "hosts_up", "scan_type", "elapsed"]),
         )
         self.assertEqual(
            d1.unchanged(), set(["hosts_down", "version", "NmapHost::127.0.0.1"])
         )
         self.assertEqual(d1.removed(), set(["NmapHost::74.207.244.221"]))
 