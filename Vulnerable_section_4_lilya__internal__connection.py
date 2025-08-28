     @property
     def headers(self) -> Header:
         if self._headers is None:
            self._headers = Header.from_scope(scope=self.scope)
         return self._headers
 
     @property