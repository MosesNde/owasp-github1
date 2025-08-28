 class TestAddIntervention(TestBrokerCommand):
 
     def test_00_bad_intervention_times(self):
        command = ["add_intervention", "--intervention=i1",
                    "--expiry=long long ago",
                    "--reason=no-good-reason",
                    "--hostname=server1.aqd-unittest.ms.com",
         self.matchoutput(out, "The expiry value 'long long ago' "
                          "could not be interpreted", command)
 
        command = ["add_intervention", "--intervention=i1",
                    "--expiry='%s'" % when,
                    "--start=long long ago",
                    "--reason=no-good-reason",
 
         too_late = datetime.utcnow().replace(microsecond=0) + timedelta(days=2)
         too_late = too_late.isoformat().replace("T", " ")
        command = ["add_intervention", "--intervention=i1",
                    "--expiry='%s'" % when,
                    "--start='%s'" % too_late,
                    "--reason=no-good-reason",
                          command)
 
     def test_05_add_basic_intervention(self):
        command = ["add_intervention", "--intervention=i1",
                    "--expiry='%s'" % when,
                    "--reason=no-good-reason",
                    "--hostname=server1.aqd-unittest.ms.com",
                    "--allowusers=testuser1",
                    "--comments=Some intervention comments"]
         self.successtest(command)
 
        command = ["show_intervention", "--intervention=i1",
                    "--hostname=server1.aqd-unittest.ms.com"]
 
         out = self.commandtest(command)
        self.matchoutput(out, "Intervention: i1", command)
         self.matchoutput(out, "Bound to: Host server1.aqd-unittest.ms.com",
                          command)
         self.matchoutput(out, "Expires: %s" % when, command)
         self.matchoutput(out, "Comments: Some intervention comments", command)
 
     def test_10_addexisting(self):
        command = ["add_intervention", "--intervention=i1",
                    "--expiry='%s'" % when,
                    "--reason=no-good-reason",
                    "--hostname=server1.aqd-unittest.ms.com",
         command = ["show_intervention",
                    "--hostname=server1.aqd-unittest.ms.com"]
         out = self.commandtest(command)
        self.matchoutput(out, "Intervention: i1", command)
         self.matchoutput(out, "Intervention: blank", command)
         self.matchoutput(out, "Intervention: groups", command)
         self.matchoutput(out, "Intervention: disable", command)
         self.notfoundtest(command.split(" "))
 
     def test_20_catintervention(self):
        command = ["cat", "--intervention=i1",
                    "--hostname=server1.aqd-unittest.ms.com"]
         out = self.commandtest(command)
         self.matchoutput(out,
                          "structure template resource"
                          "/host/server1.aqd-unittest.ms.com"
                         "/intervention/i1/config;",
                          command)
        self.matchoutput(out, '"name" = "i1";', command)
         self.matchoutput(out, '"start" =', command)
         self.matchoutput(out, '"expiry" = "%s"' % EXPIRY, command)
 
     def test_30_checkhost(self):
         command = ["show_host", "--hostname=server1.aqd-unittest.ms.com"]
         out = self.commandtest(command)
        self.matchoutput(out, "Intervention: i1", command)
 
         command = ["cat", "--generate",
                    "--hostname=server1.aqd-unittest.ms.com", "--data"]
         out = self.commandtest(command)
        self.matchoutput(out, '"system/resources/intervention" = append(create("resource/host/server1.aqd-unittest.ms.com/intervention/i1/config"))',
                          command)
 
 if __name__ == '__main__':