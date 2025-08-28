         """
         if message["type"] == "http.response.start":
             # we need to update the headers of message
            headers: Header = Header.from_scope(message)
             headers.add(
                 "Content-Security-Policy", "" if not self.content_policy else self.content_policy
             )
             headers.add("X-Content-Type-Options", self.content_type_options)
             headers.add("X-Frame-Options", self.frame_options)
             headers.add("X-XSS-Protection", self.xss_protection)
            message["headers"] = headers.encoded_multi_items()
 
         await send(message)