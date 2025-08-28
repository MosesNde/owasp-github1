 
     def multi_items(self) -> Generator[tuple[str, T], None, None]:
         """Get all keys and values, including duplicates."""
        for key in set(self):
             for value in self.getall(key):
                 yield key, value
 
     @classmethod
     def from_scope(cls, scope: Any) -> Header:
         """
        Builds the headers from the scope.
         """
         return cls(scope["headers"])
 
     def add_vary_header(self, vary: str) -> None:
         existing = self.get("vary")
         if existing is not None:
             for key, value in self.multi_items()
         )
 
     def get_encoded_multi_items(self) -> list[tuple[bytes, bytes]]:
         """
         Returns a list of values from the bytes encoded multi items for ASGI