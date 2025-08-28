         """
         if message["type"] == "http.response.start":
             # we need to update the message
            headers: Header = Header.from_scope(message)
 
             if headers.get("X-Frame-Options") is None:
                 headers.add("X-Frame-Options", self.get_xframe_options())
                message["headers"] = headers.encoded_multi_items()
         await send(message)
 
     def get_xframe_options(self) -> str: