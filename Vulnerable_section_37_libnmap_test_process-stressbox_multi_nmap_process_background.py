 #!/usr/bin/env python
 
from libnmap.process import NmapProcess
 from time import sleep
 
 
 def make_nmproc_obj(targets, options):
     return NmapProcess(targets=targets, options=options)