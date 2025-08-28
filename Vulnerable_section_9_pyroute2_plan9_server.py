 import asyncio
 import json
 
from pyroute2.netlink.core import AsyncCoreSocket, CoreConfig, CoreSocketSpec
 from pyroute2.plan9 import (
     Marshal9P,
     Plan9Exit,
         '''
         return inode.register_function(func, loader, dumper)
 
    async def setup_endpoint(self, loop=None):
        if self.endpoint is not None:
             return
         if self.status['use_socket']:
            self.endpoint = await self.event_loop.create_connection(
                lambda: Plan9ServerProtocol(
                    self.connection_lost, self.marshal, self.filesystem
                ),
                sock=self.use_socket,
             )
         else:
            self.endpoint = await self.event_loop.create_server(
                 lambda: Plan9ServerProtocol(
                     self.connection_lost, self.marshal, self.filesystem
                 ),
         '''
         await self.setup_endpoint()
         if self.status['use_socket']:
            return self.endpoint[1].on_con_lost
         else:
            return asyncio.create_task(self.endpoint.serve_forever())
 
     def run(self):
         '''A simple synchronous runner.