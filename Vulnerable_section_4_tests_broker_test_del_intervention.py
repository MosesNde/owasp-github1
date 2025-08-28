 
     def test_100_del_intervention(self):
         path = ["resource", "host", "server1.aqd-unittest.ms.com",
                "intervention", "i1", "config"]
         self.check_plenary_exists(*path)
        command = ["del_intervention", "--intervention=i1",
                    "--hostname=server1.aqd-unittest.ms.com"]
         self.successtest(command)
         self.check_plenary_gone(*path)