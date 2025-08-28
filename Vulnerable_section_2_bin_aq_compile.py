 import sys
 import os
 from subprocess import call
 
 try:
     import ms.version
     if config.has_value("broker", "ant_options"):
         panc_env["ANT_OPTS"] = config.get("broker", "ant_options")
 
    args = [config.lookup_tool("ant"), "--noconfig", "-f"]
    args.append(lookup_file_path("build.xml"))
    args.append("-Dbasedir=%s" % options.basedir)
 
     if options.swrep:
         args.append("-Dswrep=%s" % options.swrep)