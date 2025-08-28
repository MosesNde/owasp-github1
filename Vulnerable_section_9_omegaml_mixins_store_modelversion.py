         return actual_name
 
     def _model_version_hash(self, meta):
         hasher = sha1()
         hasher.update(_u8(meta.name))
         hasher.update(_u8(str(meta.modified)))