 from lib.common_config import (
     required_linux_kernel_version,
 )
from lib.topolog import logger
 
 import json
 import functools
 
     test_func = functools.partial(get_func, route_str)
     _, nhg_id = topotest.run_and_expect_type(test_func, int, count=30, wait=1)
    if nhg_id == None:
         fatal_error = "Nexthop Group ID not found for route {}".format(route_str)
        assert nhg_id != None, fatal_error
     else:
         return nhg_id
 
         refTableFile = "{}/r{}/rip_status.ref".format(thisDir, i)
         if os.path.isfile(refTableFile):
             # Read expected result from file
            expected = open(refTableFile).read().rstrip()
             # Fix newlines (make them all the same)
             expected = ("\n".join(expected.splitlines()) + "\n").splitlines(1)
 
         refTableFile = "{}/r{}/ripng_status.ref".format(thisDir, i)
         if os.path.isfile(refTableFile):
             # Read expected result from file
            expected = open(refTableFile).read().rstrip()
             # Fix newlines (make them all the same)
             expected = ("\n".join(expected.splitlines()) + "\n").splitlines(1)
 
         refTableFile = "{}/r{}/show_ip_ospf_interface.ref".format(thisDir, i)
         if os.path.isfile(refTableFile):
             # Read expected result from file
            expected = open(refTableFile).read().rstrip()
             # Fix newlines (make them all the same)
             expected = ("\n".join(expected.splitlines()) + "\n").splitlines(1)
 
         refTableFile = "{}/r{}/show_isis_interface_detail.ref".format(thisDir, i)
         if os.path.isfile(refTableFile):
             # Read expected result from file
            expected = open(refTableFile).read().rstrip()
             # Fix newlines (make them all the same)
             expected = ("\n".join(expected.splitlines()) + "\n").splitlines(1)
 
         refTableFile = "{}/r{}/show_ip_bgp_summary.ref".format(thisDir, i)
         if os.path.isfile(refTableFile):
             # Read expected result from file
            expected_original = open(refTableFile).read().rstrip()
 
             for arguments in [
                 "",
         refTableFile = "{}/r{}/show_bgp_ipv6_summary.ref".format(thisDir, i)
         if os.path.isfile(refTableFile):
             # Read expected result from file
            expected = open(refTableFile).read().rstrip()
             # Fix newlines (make them all the same)
             expected = ("\n".join(expected.splitlines()) + "\n").splitlines(1)
 
 
     for i in range(1, 2):
         nhtFile = "{}/r{}/ip_nht.ref".format(thisDir, i)
        expected = open(nhtFile).read().rstrip()
         expected = ("\n".join(expected.splitlines()) + "\n").splitlines(1)
 
         actual = (
             print("show ip nht is ok\n")
 
         nhtFile = "{}/r{}/ipv6_nht.ref".format(thisDir, i)
        expected = open(nhtFile).read().rstrip()
         expected = ("\n".join(expected.splitlines()) + "\n").splitlines(1)
 
         actual = (
         for refTableFile in glob.glob("{}/r{}/show_bgp_ipv4*.ref".format(thisDir, i)):
             if os.path.isfile(refTableFile):
                 # Read expected result from file
                expected = open(refTableFile).read().rstrip()
                 # Fix newlines (make them all the same)
                 expected = ("\n".join(expected.splitlines()) + "\n").splitlines(1)
 
         for refTableFile in glob.glob("{}/r{}/show_bgp_ipv6*.ref".format(thisDir, i)):
             if os.path.isfile(refTableFile):
                 # Read expected result from file
                expected = open(refTableFile).read().rstrip()
                 # Fix newlines (make them all the same)
                 expected = ("\n".join(expected.splitlines()) + "\n").splitlines(1)
 
     for i in range(1, 2):
         refroutemap = "{}/r{}/show_route_map.ref".format(thisDir, i)
         if os.path.isfile(refroutemap):
            expected = open(refroutemap).read().rstrip()
             expected = ("\n".join(expected.splitlines()) + "\n").splitlines(1)
 
             actual = (
         refTableFile = "{}/r{}/show_mpls_ldp_interface.ref".format(thisDir, i)
         if os.path.isfile(refTableFile):
             # Read expected result from file
            expected = open(refTableFile).read().rstrip()
             # Fix newlines (make them all the same)
             expected = ("\n".join(expected.splitlines()) + "\n").splitlines(1)
 