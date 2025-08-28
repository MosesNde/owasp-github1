             receive (Receive): ASGI receive channel.
             send (Send): ASGI send channel.
         """
        headers: Header = Header.from_scope(scope)
         scope["real-clientip"] = headers["x-real-ip"] = get_ip(
             scope, trusted_proxies=self.trusted_proxies
         )
        scope["headers"] = headers.encoded_multi_items()
 
         await self.app(scope, receive, send)