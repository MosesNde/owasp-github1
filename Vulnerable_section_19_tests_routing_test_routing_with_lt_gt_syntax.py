 
         async def modified_send(msg: Message) -> None:
             if msg["type"] == "http.response.start":
                msg["headers"].append((b"X-Test", b"Set by middleware"))
             await send(msg)
 
         await self.app(scope, receive, modified_send)
         async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
             async def modified_send(msg: Message) -> None:
                 if msg["type"] == "http.response.start":
                    msg["headers"].append((f"X-{self.name}".encode(), b"true"))
                 await send(msg)
 
             await self.app(scope, receive, modified_send)
         async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
             async def modified_send(msg: Message) -> None:
                 if msg["type"] == "websocket.accept":
                    msg["headers"].append((b"X-Test", b"Set by middleware"))
                 await send(msg)
 
             await self.app(scope, receive, modified_send)