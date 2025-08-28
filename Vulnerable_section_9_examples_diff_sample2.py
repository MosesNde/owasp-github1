 
 
 def main():
    newrep = NmapParser.parse_fromfile("libnmap/test/files/2_hosts_achange.xml")
     oldrep = NmapParser.parse_fromfile("libnmap/test/files/1_hosts.xml")
 
     print_diff(newrep, oldrep)