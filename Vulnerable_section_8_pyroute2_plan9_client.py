 from pyroute2.netlink.core import (
     AsyncCoreSocket,
     CoreConfig,
     CoreSocketSpec,
     CoreStreamProtocol,
 )
         tag = struct.unpack_from('H', data, 5)[0]
         return self.msg_queue.put_nowait(tag, data)
 
    def setup_socket(self, sock=None):
        return sock

     async def setup_endpoint(self, loop=None):
        if self.endpoint is not None:
             return
         if self.status['use_socket']:
             address = {'sock': self.use_socket}
         else:
             address = {
                 'host': self.status['address'][0],
                 'port': self.status['address'][1],
             }
        self.endpoint = await self.event_loop.create_connection(
            lambda: CoreStreamProtocol(
                self.connection_lost,
                self.enqueue,
                self._error_event,
                self.status,
            ),
            **address,
         )
 
     async def start_session(self):
         '''Initiate 9p2000 session.
 
         One must await this routine before running any other requests.
         '''
        await self.ensure_socket()
         await self.version()
         await self.auth()
         await self.attach()
 
     async def request(self, msg, tag=0):
        await self.ensure_socket()
         if tag == 0:
             tag = self.addr_pool.alloc()
         try:
             msg['header']['tag'] = tag
             msg.reset()
             msg.encode()
             self.msg_queue.ensure_tag(tag)
            self.endpoint[0].write(msg.data)
             return [x async for x in self.get(msg_seq=tag)][0]
         finally:
             self.addr_pool.free(tag, ban=0xFF)