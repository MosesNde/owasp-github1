     ipr = AsyncIPRoute(netns=uifname())
     ts_start = time.time()
     with pytest.raises(TimeoutError):
        await ipr.ensure_socket()
     assert time.time() - ts_start < 2