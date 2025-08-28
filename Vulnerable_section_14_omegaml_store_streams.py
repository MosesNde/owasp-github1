         return stream
 
     def _cached_get(self, name, reload=False, _cachex=None):
         if reload:
             # force to avoid cache
             return self.get(name, _cachex=md5().hexdigest())