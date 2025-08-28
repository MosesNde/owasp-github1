 from pyroute2.netlink import NLM_F_MULTI
 from pyroute2.requests.main import RequestFilter, RequestProcessor
 
 log = logging.getLogger(__name__)
 Stats = collections.namedtuple('Stats', ('qsize', 'delta', 'delay'))
 CoreSocketResources = collections.namedtuple(
 )
 
 
 @dataclass
 class CoreConfig:
     target: str = 'localhost'
 
 class CoreMessageQueue:
 
    def __init__(self):
         self.queues = {0: asyncio.Queue()}
         self.root = self.queues[0]
 
     def connection_made(self, transport):
         self.transport = transport
 
    def connection_lost(self, exc):
         self.on_con_lost.set_result(True)
        self.enqueue(
            struct.pack('IHHQIQQ', 28, 2, 0, 0, errno.ECONNRESET, 0, 0), None
        )
 
    def error_received(self, exc):
         self.status['error'] = exc
         self.error_event.set()
        self.enqueue(
            struct.pack('IHHQIQQ', 28, 2, 0, 0, exc.errno, 0, 0), None
        )
 
 
 class CoreStreamProtocol(CoreProtocol):
             )
         )
         self.status = self.spec.status
         self.local = threading.local()
         self.lock = threading.Lock()
         self.libc = libc
         self.use_socket = use_socket
         self.use_event_loop = use_event_loop
         self.request_proxy = None
        self._tid = id(threading.current_thread())
         self._error_event = threading.Event()
        if use_event_loop:
            self.local.event_loop = use_event_loop
            self.local.connection_lost = self.local.event_loop.create_future()
            self.status['event_loop'] = id(use_event_loop)
            self.status['thread_id'] = id(threading.current_thread())
         url = parse.urlparse(self.spec['target'])
         self.scheme = url.scheme if url.scheme else url.path
         self.callbacks = []  # [(predicate, callback, args), ...]
         self.addr_pool = AddrPool(minaddr=0x000000FF, maxaddr=0x0000FFFF)
         self.marshal = None
         self.buffer = []
         self.msg_reschedule = []
        self.__all_open_resources = {}
 
     def get_loop(self):
         return self.event_loop
 
     @property
     def connection_lost(self):
         return self.local.connection_lost
 
     @property
    def event_loop(self):
        return self.ensure_event_loop()
 
    def ensure_event_loop(self):
         if not hasattr(self.local, 'event_loop'):
            if self.status['use_event_loop'] and self.status[
                'thread_id'
            ] != id(threading.current_thread()):
                raise RuntimeError(
                    'Predefined event loop can not be used in another thread'
                 )
             self.local.event_loop = self.setup_event_loop()
            self.local.connection_lost = self.local.event_loop.create_future()
         if self.local.event_loop.is_closed():
             raise OSError(errno.EBADF, 'Bad file descriptor')
         return self.local.event_loop
 
    async def ensure_socket(self):
        if self._error_event.is_set():
            raise self.status['error']
        if not hasattr(self.local, 'socket'):
            self.local.socket = None
            self.local.fileno = None
            self.local.msg_queue = CoreMessageQueue()
            # 8<-----------------------------------------
            self.local.socket = self.setup_socket()
            if self.spec['netns'] is not None and config.mock_netlink:
                self.local.socket.netns = self.spec['netns']
                self.local.socket.flags = self.spec['flags']
                self.local.socket.initdb()

            await self.setup_endpoint()
            self.__all_open_resources[id(threading.current_thread())] = (
                CoreSocketResources(
                    self.local.socket,
                    self.local.msg_queue,
                    self.local.event_loop,
                    self.local.endpoint[0],
                    self.local.endpoint[1],
                )
            )

     @property
    def socket(self):
        return self.local.socket
 
     @property
    def endpoint(self):
        if not hasattr(self.local, 'endpoint'):
            self.local.endpoint = None
        return self.local.endpoint

    @endpoint.setter
    def endpoint(self, value):
        self.local.endpoint = value
 
     # 8<--------------------------------------------------------------

    async def setup_endpoint(self, loop=None):
        # Setup asyncio
        if self.endpoint is not None:
            return
        self.endpoint = await self.event_loop.connect_accepted_socket(
            lambda: CoreStreamProtocol(
                self.connection_lost,
                self.enqueue,
                self._error_event,
                self.status,
            ),
            sock=self.socket,
        )

     def setup_event_loop(self):
         try:
             event_loop = asyncio.get_running_loop()
             self.status['event_loop'] = 'auto'
         except RuntimeError:
             event_loop = asyncio.new_event_loop()
             self.status['event_loop'] = 'new'
         return event_loop
 
    def setup_socket(self, sock=None):
         if self.use_socket is not None:
             return self.use_socket
        sock = self.socket if sock is None else sock
        if sock is not None:
            sock.close()
         sock = netns.create_socket(
             self.spec['netns'],
             socket.AF_INET,
         sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
         return sock
 
     def __getattr__(self, attr):
         if attr in (
             'getsockname',
 
     async def bind(self, addr):
         '''Bind the socket to the address.'''
        await self.ensure_socket()
         return self.socket.bind(addr)
 
     def close(self, code=errno.ECONNRESET):
         def send_terminator(msg_queue):
             msg_queue.put_nowait(0, b'')
 
        tid = id(threading.current_thread())
         with self.lock:
            for r in self.__all_open_resources.values():
                r.event_loop.call_soon_threadsafe(send_terminator, r.msg_queue)

            if tid not in self.__all_open_resources:
                return

            sock, msg_queue, event_loop, transport, protocol = (
                self.__all_open_resources.pop(tid)
            )
            # event_loop.call_soon(send_terminator, msg_queue)
            transport.close()
            if sock is not None:
                sock.close()
             if self.status['event_loop'] == 'new':
                # go to the event loop to really close the transport
                event_loop.run_until_complete(event_loop.shutdown_asyncgens())
                event_loop.stop()
                event_loop.close()
 
     def clone(self):
         '''Return a copy of itself with a new underlying socket.
         self, msg_seq=0, terminate=None, callback=None, noraise=False
     ):
         '''Get a conversation answer from the socket.'''
        await self.ensure_socket()
         log.debug(
             "get: %s / %s / %s / %s", msg_seq, terminate, callback, noraise
         )
             'status',
             'send',
             'recv',
             'sendto',
             'setsockopt',
             'getsockopt',
             return getattr(self.asyncore, key)
         raise AttributeError(key)
 
     def mock_data(self, data):
         if getattr(self.asyncore.local, 'msg_queue', None) is None:
            self.asyncore.local.msg_queue = CoreMessageQueue()
         self.asyncore.msg_queue.put_nowait(0, data)
 
     def close(self, code=errno.ECONNRESET):
         self,
         target='localhost',
         rcvsize=16384,
        use_socket=False,
         netns=None,
         flags=os.O_CREAT,
         libc=None,
         self.asyncore = AsyncCoreSocket(
             target, rcvsize, use_socket, netns, flags, libc, groups
         )