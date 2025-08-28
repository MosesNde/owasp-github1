 
 import importlib.util
 import os
 import stat
 from email.utils import parsedate
 from typing import Union
         Returns:
             str: Normalized path.
         """
        route_path = self.get_route_path(scope)
         return os.path.normpath(os.path.join(*route_path.split("/")))
 
     def get_route_path(self, scope: Scope) -> str:
         """
         if scope["method"] not in ("GET", "HEAD"):
             raise HTTPException(status_code=405)

         try:
             full_path, stat_result = await anyio.to_thread.run_sync(self.lookup_path, path)
         except PermissionError:
         Returns:
             Response: File response.
         """
        try:
            request_headers = Header.from_scope(scope=scope)
        except KeyError:
            raise HTTPException(status_code=404) from None
 
         response = FileResponse(full_path, status_code=status_code, stat_result=stat_result)
         if self.is_not_modified(response.headers, request_headers):