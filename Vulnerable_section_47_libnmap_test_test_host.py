 # -*- coding: utf-8 -*-
 
 import unittest
 from libnmap.parser import NmapParser
 
 host1 = """
         h2 = NmapParser.parse(host2)
 
         self.assertEqual(
            h1.extraports_state["state"], {"count": "995", "state": "WILLY_WONCKA"}
         )
         self.assertEqual(
             h1.extraports_reasons, [{"reason": "conn-refused", "count": "995"}]
             ),
         )
 
        self.assertEqual(c2.changed(), set(["status", "NmapService::tcp.3306"]))
         self.assertEqual(c2.added(), set(["NmapService::tcp.25"]))
         self.assertEqual(c2.removed(), set(["NmapService::tcp.3307"]))
         self.assertEqual(