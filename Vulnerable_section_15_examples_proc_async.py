 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
 
from libnmap.process import NmapProcess
 from time import sleep
 
 
 nmap_proc = NmapProcess(targets="scanme.nmap.org", options="-sT")
 nmap_proc.run_background()