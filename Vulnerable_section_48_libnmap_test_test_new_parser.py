 # -*- coding: utf-8 -*-
 
 import unittest
 from libnmap.parser import NmapParser, NmapParserException
 
 baddatalist = [
 class TestNmapParser(unittest.TestCase):
     def test_parse(self):
         for baddata in baddatalist:
            self.assertRaises(NmapParserException, NmapParser.parse, baddata, "zz")
            self.assertRaises(NmapParserException, NmapParser.parse, baddata, "XML")
            self.assertRaises(NmapParserException, NmapParser.parse, baddata, "YAML")
 
 
 if __name__ == "__main__":