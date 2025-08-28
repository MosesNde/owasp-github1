 def test_no_free_ports():
     soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
     try:
        resource.setrlimit(resource.RLIMIT_NOFILE, (4096, 4096))
     except ValueError:
         pytest.skip('cannot set RLIMIT_NOFILE')
 