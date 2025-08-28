 
 CACHE_RESPONSE = True
 
 # This MUST BE THE LAST!
 if os.path.isfile(os.path.join(BASE_DIR, "config_local.py")):
     from config_local import *  # noqa # flake8: noqa # NOQA # pragma: no cover