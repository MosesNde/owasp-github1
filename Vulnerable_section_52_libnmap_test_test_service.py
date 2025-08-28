 # -*- coding: utf-8 -*-
 
 import unittest
from libnmap.parser import NmapParser
 from libnmap.diff import NmapDiffException
 
 service1 = """
 <port protocol="tcp" portid="22">
         self.assertRaises(NmapDiffException, nservice1.diff, nservice4)
         #
         self.assertRaises(NmapDiffException, nservice2.diff, nservice3)
        self.assertEqual(nservice3.diff(nservice4).changed(), set(["state", "service"]))
 
     def test_port_state_unchanged(self):
         nservice1 = NmapParser.parse(port_string)