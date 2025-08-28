                             source_name,
                             cache_dir, debug, wait_on_error, debug_recompile,
                             False)
     # try loading it
     from imp import load_dynamic
     return load_dynamic(mod_name, ext_file)
 
     from os.path import join
 
     if cache_dir is None:
        from tempfile import gettempdir
        cache_dir = join(gettempdir(),
                "codepy-compiler-cache-v5-uid%s" % os.getuid())
 
         try:
            os.mkdir(cache_dir)
         except OSError, e:
             from errno import EEXIST
             if e.errno != EEXIST: