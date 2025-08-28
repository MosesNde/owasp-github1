     return create_db()
 
 
 def pack_kv_entry(
     key: AnyKvKey, value: bytes, versionstamp: int = 1
 ) -> ProtobufKvEntry:
     assert session.closed
 
 
def test_close_via_finalizer__loop_not_running() -> None:
    loop = asyncio.new_event_loop()
     authenticator = Mock()
 
     async def create_session() -> aiohttp.ClientSession: