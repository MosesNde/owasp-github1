         hashed = hashed if hashed is not None else self.defaults.OMEGA_STORE_HASHEDNAMES
         if hashed:
             from hashlib import sha1
             hasher = sha1()
             hasher.update(_u8(key))
             key = hasher.hexdigest()