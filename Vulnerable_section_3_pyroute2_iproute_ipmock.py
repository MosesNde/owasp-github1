 from pyroute2.netlink.rtnl.rtmsg import rtmsg
 
 interface_counter = count(3)
 
 
 class MockLink:
         self.marshal = MarshalRtnl()
         self.netns = netns
         self.flags = flags
         self._stype = stype
         self._sfamily = sfamily
         self._sproto = sproto
         self.database = copy.deepcopy(presets[self.netns])
 
     def close(self):
        self.loopback_r.close()
        self.loopback_w.close()
 
     def bind(self, address=None):
         self._broadcast.add(self.loopback_w)