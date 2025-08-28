     def test_030_search_intervention(self):
         command = ['search_intervention', '--hostname', 'server1.aqd-unittest.ms.com']
         out = self.commandtest(command)
        self.matchoutput(out, 'Intervention: i1', command)
         self.matchoutput(out, 'Intervention: blank', command)
         self.matchoutput(out, 'Intervention: groups', command)
         self.matchoutput(out, 'Intervention: disable', command)