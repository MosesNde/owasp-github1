             libc=libc,
             use_event_loop=use_event_loop,
         )
        self.asyncore.ensure_event_loop()
        if self.asyncore.status['event_loop'] != 'new' and not use_event_loop:
            raise RuntimeError()
         self.asyncore.event_loop.run_until_complete(
            self.asyncore.ensure_socket()
         )
 
     @classmethod
     def from_asyncore(cls, iproute):
                 task = collect_dump
             else:
                 task = collect_op
            return self.event_loop.run_until_complete(task())
 
         def synchronize_dump(*argv, **kwarg):
             async def collect_dump():
                 return [i async for i in await symbol(*argv, **kwarg)]
 
            return self.event_loop.run_until_complete(collect_dump())
 
         if name in async_generic_methods:
            return synchronize_generic
         elif name in async_dump_methods:
            return synchronize_dump
         return symbol
 
 