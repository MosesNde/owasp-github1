             "type": prefix + "http.response.start",
             "status": self.status_code,
             # some tests add headers dirty and assume a list
            "headers": self.headers.get_encoded_multi_items(),
         }
 
     async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None: