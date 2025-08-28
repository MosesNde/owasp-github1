 #!/usr/bin/env python
from libnmap.process import NmapProcess
 from libnmap.parser import NmapParser, NmapParserException
 
 nm = NmapProcess("127.0.0.1", "-sP")
 rc = nm.run()