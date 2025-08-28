 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
 
import unittest
 import os
 from libnmap.parser import NmapParser
 
 
 class TestNmapFP(unittest.TestCase):
     def setUp(self):
         fdir = os.path.dirname(os.path.realpath(__file__))
         self.flist_full = [
            {"file": "%s/%s" % (fdir, "files/1_os_banner_scripts.xml"), "os": 1},
             {"file": "%s/%s" % (fdir, "files/2_hosts_version.xml"), "os": 1},
             {
                "file": "%s/%s" % (fdir, "files/1_hosts_banner_ports_notsyn.xml"),
                 "os": 0,
             },
             {"file": "%s/%s" % (fdir, "files/1_hosts_banner.xml"), "os": 0},
         self.flist = self.flist_full
         self.flist_os = {
             "nv6": {"file": "%s/%s" % (fdir, "files/full_sudo6.xml"), "os": 0},
            "fullscan": {"file": "%s/%s" % (fdir, "files/fullscan.xml"), "os": 0},
             "nv5": {"file": "%s/%s" % (fdir, "files/os_scan5.xml"), "os": 0},
         }
        self.fos_class_probabilities = "{0}/{1}".format(fdir, "files/test_osclass.xml")
 
     def test_fp(self):
         for file_e in self.flist_full:
                     "accuracy": 100,
                     "name": "Microsoft Windows 7 Professional",
                 },
                {"line": 54362, "accuracy": 100, "name": "Microsoft Windows Phone 7.5"},
                 {
                     "line": 54897,
                     "accuracy": 100,
         j = 0
         for h in hlist:
             for om in h.os.osmatches:
                tdict = {"line": om.line, "accuracy": om.accuracy, "name": om.name}
                 self.assertEqual(baseline[i][j], tdict)
                 j += 1
             j = 0
         rep = NmapParser.parse_fromfile(self.flist_os["nv5"]["file"])
         h1 = rep.hosts[4]
         h1osmatches = [
            {"line": -1, "accuracy": 95, "name": "general purpose:Linux:Linux"},
             {"line": -1, "accuracy": 90, "name": "WAP:Gemtek:embedded"},
            {"line": -1, "accuracy": 89, "name": "general purpose:Nokia:Linux"},
             {"line": -1, "accuracy": 88, "name": "webcam:AXIS:Linux"},
         ]
 