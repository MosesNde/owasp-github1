         'port': 0,
         'uname': config.uname,
         'use_socket': False,
     }
     status_filters = [NetlinkSocketSpecFilter]
 
         self.request_proxy = None
         self.batch = None
 
    async def setup_endpoint(self, loop=None):
        # Setup asyncio
        if self.endpoint is not None:
             return
        self.endpoint = await self.event_loop.create_datagram_endpoint(
            lambda: CoreDatagramProtocol(
                self.connection_lost,
                self.enqueue,
                self._error_event,
                self.status,
            ),
            sock=self.socket,
         )
 
     @property
     def uname(self):
         return self.status['uname']
     def target(self):
         return self.status['target']
 
    def setup_socket(self, sock=None):
        """Re-init a netlink socket."""
        if self.status['use_socket']:
            return self.use_socket
        sock = self.socket if sock is None else sock
        if sock is not None:
            sock.close()
        sock = netns.create_socket(
            self.spec['netns'],
            AF_NETLINK,
            SOCK_DGRAM,
            self.spec['family'],
            self.spec['fileno'] or self.local.fileno,
            self.spec['flags'],
            self.libc,
        )
        sock.setsockopt(SOL_SOCKET, SO_SNDBUF, self.status['sndbuf'])
        sock.setsockopt(SOL_SOCKET, SO_RCVBUF, self.status['rcvbuf'])
        if self.status['ext_ack']:
            sock.setsockopt(SOL_NETLINK, NETLINK_EXT_ACK, 1)
        if self.status['all_ns']:
            sock.setsockopt(SOL_NETLINK, NETLINK_LISTEN_ALL_NSID, 1)
        if self.status['strict_check']:
            sock.setsockopt(SOL_NETLINK, NETLINK_GET_STRICT_CHK, 1)
        return sock

    async def bind(self, groups=0, pid=None, **kwarg):
        '''
        Bind the socket to given multicast groups, using
        given pid.

            - If pid is None, use automatic port allocation
            - If pid == 0, use process' pid
            - If pid == <int>, use the value instead of pid
        '''
        await self.ensure_socket()
         self.spec['groups'] = groups
         # if we have pre-defined port, use it strictly
         self.spec['pid'] = pid
             else:
                 raise KeyError('no free address available')
 
     def add_membership(self, group):
         self.socket.setsockopt(SOL_NETLINK, NETLINK_ADD_MEMBERSHIP, group)
 
         return True
 
     async def send(self):
        await self.sock.ensure_socket()
         self.msg.encode()
         self.sock.msg_queue.ensure_tag(self.msg_seq)
         if self.parser is not None:
             use_socket=use_socket,
             use_event_loop=use_event_loop,
         )

    @property
    def fileno(self):
        return self.asyncore.socket.fileno
 
     def bind(self, *argv, **kwarg):
        return self.asyncore.event_loop.run_until_complete(
            self.asyncore.bind(*argv, **kwarg)
        )
 
     def put(
         self,
         if msg is None:
             msg_class = self.marshal.msg_map[msg_type]
             msg = msg_class()
        return self.asyncore.event_loop.run_until_complete(
            self.asyncore.put(msg, msg_type, msg_flags, addr, msg_seq, msg_pid)
         )
 
     def nlm_request(
                 )
             ]
 
        return self.asyncore.event_loop.run_until_complete(collect_data())
 
     def get(self, msg_seq=0, terminate=None, callback=None, noraise=False):
         '''Sync wrapper for async_get().'''
                 )
             ]
 
        return self.asyncore.event_loop.run_until_complete(collect_data())
 
 
 class ChaoticNetlinkSocket(NetlinkSocket):