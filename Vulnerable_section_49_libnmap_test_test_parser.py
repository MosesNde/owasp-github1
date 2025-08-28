 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
 
import unittest
 import os
 from libnmap.parser import NmapParser, NmapParserException
 
 
             {"file": "%s/%s" % (fdir, "files/2_hosts.xml"), "hosts": 2},
             {"file": "%s/%s" % (fdir, "files/1_hosts.xml"), "hosts": 1},
             {
                "file": "%s/%s" % (fdir, "files/1_hosts_banner_ports_notsyn.xml"),
                 "hosts": 1,
             },
             # {'file': "%s/%s" % (fdir,
             #                      'files/1_hosts_banner_ports_xmas.xml'),
             #                      'hosts': 1},
            {"file": "%s/%s" % (fdir, "files/1_hosts_banner_ports.xml"), "hosts": 1},
             {"file": "%s/%s" % (fdir, "files/1_hosts_banner.xml"), "hosts": 1},
            {"file": "%s/%s" % (fdir, "files/2_hosts_version.xml"), "hosts": 2},
             # {'file': "%s/%s" % (fdir,
             #                      'files/2_null_hosts.xml'), 'hosts': 2},
             {"file": "%s/%s" % (fdir, "files/2_tcp_hosts.xml"), "hosts": 2},
            {"file": "%s/%s" % (fdir, "files/1_hosts_nohostname.xml"), "hosts": 1},
         ]
         self.flist = self.flist_full
 
         pdict = NmapParser.parse(self.ports_string)
         plist = pdict["ports"]
         self.assertEqual(len(plist), 4)
        self.assertEqual(sorted([p.port for p in plist]), sorted([22, 25, 9929, 80]))
         self.assertRaises(ValueError, NmapParser.parse, self.ports_string2)
 
     def test_class_port_parser(self):
 
     def test_port_except(self):
         self.assertRaises(ValueError, NmapParser.parse, self.port_string2)
        self.assertRaises(NmapParserException, NmapParser.parse, self.port_string3)
        self.assertRaises(NmapParserException, NmapParser.parse, self.port_string4)
        self.assertRaises(NmapParserException, NmapParser.parse, self.port_string5)
         self.assertRaises(ValueError, NmapParser.parse, self.port_string6)
        self.assertRaises(NmapParserException, NmapParser.parse, self.port_string7)
        self.assertRaises(NmapParserException, NmapParser.parse, self.port_string8)
         serv = NmapParser.parse(self.port_string9)
         self.assertEqual(serv.state, None)
 