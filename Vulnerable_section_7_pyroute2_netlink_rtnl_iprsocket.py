 from pyroute2 import config
 from pyroute2.common import msg_done
 from pyroute2.iproute.ipmock import IPEngine
from pyroute2.netlink import NETLINK_ROUTE, nlmsg, rtnl
 from pyroute2.netlink.exceptions import NetlinkError
 from pyroute2.netlink.nlsocket import (
     AsyncNetlinkSocket,
     ChaoticNetlinkSocket,
     NetlinkSocket,
 )
 from pyroute2.netlink.rtnl.ifinfmsg.tuntap import manage_tun, manage_tuntap
     ):
         if config.mock_netlink:
             use_socket = IPEngine()
         self.marshal = MarshalRtnl()
         super().__init__(
             family=NETLINK_ROUTE,
 
 class NotLocal:
     event_loop = None
    socket = None
    fileno = None
     msg_queue = mock.Mock()
 
 
             use_event_loop=use_event_loop,
         )
         self.asyncore.local = NotLocal()
        self.asyncore.local.event_loop = self.asyncore.setup_event_loop()
        self.asyncore.local.socket = self.asyncore.setup_socket()
 
     @property
     def socket(self):
        return self.asyncore.local.socket
 
     @property
     def fileno(self):
         return self.asyncore.local.socket.fileno
 
     def get(self, msg_seq=0, terminate=None, callback=None, noraise=False):
         data = self.socket.recv(16384)
         return [x for x in self.marshal.parse(data)]