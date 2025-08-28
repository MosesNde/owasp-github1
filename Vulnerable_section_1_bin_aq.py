 
 import sys
 import os
 import re
 import subprocess
 import socket
             print(pageData)
         else:
             try:
                proc = subprocess.Popen(pageData, shell=True, stdin=sys.stdin,
                                        stdout=sys.stdout, stderr=sys.stderr)
             except OSError as e:
                 print(str(e), file=sys.stderr)
                 sys.exit(1)
         if int(res.headers.get("Content-Length", 0)) > 0 and res.headers.get("Content-Type", "").startswith('text/'):
                 # TODO: honour the charset in the header, if any - not that the
                 # broker would use anything else
                # if isinstance(pageData, bytes):
                #     pageData = str(pageData, "utf-8")
                # pageData = str(pageData, "utf-8")
                 pageData = pageData.decode("utf-8")
                 sys.stdout.write(pageData)
                 # The CSV formatter adds a terminating newline, raw formatters not