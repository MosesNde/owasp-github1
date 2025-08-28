     """
     # avoid generating a name if already given
     if not 'name' in kwargs:
         name = md5(str(idx).encode('utf8')).hexdigest()
         kwargs.setdefault('name', name)
     return idx, kwargs