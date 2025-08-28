   lock.acquire()
 
   try:
    tmp_path = tempfile.mktemp(prefix=".tmp", dir=params_path)
    with open(tmp_path, "wb") as f:
       f.write(value)
       f.flush()
       os.fsync(f.fileno())
 
     path = "%s/d/%s" % (params_path, key)
    os.rename(tmp_path, path)
     fsync_dir(os.path.dirname(path))
   finally:
     os.umask(prev_umask)