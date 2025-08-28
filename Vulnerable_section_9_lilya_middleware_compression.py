             send: The ASGI send function.
         """
         if scope["type"] == "http":
            headers = Header.from_scope(scope=scope)
             if "gzip" in headers.get("Accept-Encoding", ""):
                 responder = GZipResponder(
                     self.app, self.minimum_size, compresslevel=self.compresslevel
             message (Message): The outgoing message.
         """
         self.initial_message = message
        headers = Header(self.initial_message["headers"])
         self.content_encoding_set = "content-encoding" in headers
 
     async def handle_response_body_with_encoding(self, message: Message) -> None:
         self.gzip_file.close()
         body = self.gzip_buffer.getvalue()
 
        headers = Header(self.initial_message["headers"])
         headers["Content-Encoding"] = "gzip"
         headers["Content-Length"] = str(len(body))
         headers.add_vary_header("Accept-Encoding")
         message["body"] = body
 
        self.initial_message["headers"] = headers.encoded_multi_items()
         await self.send(self.initial_message)
         await self.send(message)
 
             body (bytes): The response body.
             message (Message): The outgoing message.
         """
        headers = Header(self.initial_message["headers"])
         headers["Content-Encoding"] = "gzip"
         headers.add_vary_header("Accept-Encoding")
 
         self.gzip_buffer.seek(0)
         self.gzip_buffer.truncate()
 
        self.initial_message["headers"] = headers.encoded_multi_items()
         await self.send(self.initial_message)
         await self.send(message)
 