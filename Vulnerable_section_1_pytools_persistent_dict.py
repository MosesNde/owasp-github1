 
         from os.path import join
         if container_dir is None:
            from tempfile import gettempdir
            import getpass
            container_dir = join(gettempdir(),
                    "pytools-pdict-%s-uid%s-py%s" % (
                         identifier,
                        getpass.getuser(),
                        ".".join(str(i) for i in sys.version_info)))
 
         self.container_dir = container_dir
 
         # {{{ ensure container directory exists
 
         try:
            os.mkdir(self.container_dir)
         except OSError, e:
             from errno import EEXIST
             if e.errno != EEXIST: