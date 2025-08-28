 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
 
import unittest
 import os
 
 # sys.path.append("".join([os.path.dirname(__file__), "/../"]))
 from libnmap.parser import NmapParser
from libnmap.diff import NmapDiffException
 
 
 class TestNmapParser(unittest.TestCase):
             {"file": "%s/%s" % (fdir, "files/2_hosts.xml"), "hosts": 2},
             {"file": "%s/%s" % (fdir, "files/1_hosts.xml"), "hosts": 1},
             {
                "file": "%s/%s" % (fdir, "files/1_hosts_banner_ports_notsyn.xml"),
                 "hosts": 1,
             },
            {"file": "%s/%s" % (fdir, "files/1_hosts_banner_ports.xml"), "hosts": 1},
             {"file": "%s/%s" % (fdir, "files/1_hosts_banner.xml"), "hosts": 1},
            {"file": "%s/%s" % (fdir, "files/2_hosts_version.xml"), "hosts": 2},
             {"file": "%s/%s" % (fdir, "files/2_tcp_hosts.xml"), "hosts": 2},
            {"file": "%s/%s" % (fdir, "files/1_hosts_nohostname.xml"), "hosts": 1},
         ]
 
         self.flist_one = [
            {"file": "%s/%s" % (fdir, "files/1_hosts_nohostname.xml"), "hosts": 1}
         ]
         self.flist_two = [
             {
                 "banner": {
                     "631": "product: CUPS version: 1.4",
                     "3306": "product: MySQL version: 5.1.61",
                    "22": ("product: OpenSSH version: 5.3" " extrainfo: protocol 2.0"),
                    "25": ("product: Postfix smtpd" " hostname:  jambon.localdomain"),
                     "111": "",
                 },
             }
             self.assertEqual(len(nr.hosts), testfile["hosts"])
 
             self.assertEqual(len(nr2.hosts), testfile["hosts"])
            self.assertEqual(sorted(nr2.get_raw_data()), sorted(nr.get_raw_data()))
 
     def test_get_ports(self):
         for testfile in self.flist:
             nr = NmapParser.parse(s)
             self.assertEqual(getattr(nr, "endtime"), int(testfile["endtime"]))
             self.assertEqual(getattr(nr, "summary"), testfile["summary"])
            self.assertEqual(getattr(nr, "elapsed"), float(testfile["elapsed"]))
 
     def test_banner(self):
         for testfile in self.flist_banner:
             """All the service of the host must be compared and
                the hash should be also the same"""
             for i in range(len(host1.services)):
                self.assertEqual(hash(host1.services[i]), hash(host2.services[i]))
                 self.assertEqual(host1.services[i], host2.services[i])
 
             # print host1.serviceChanged(host2)