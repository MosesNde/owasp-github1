 
 
 def test_fileno():
    ipr1 = IPRoute()
    ipr2 = IPRoute(fileno=ipr1.fileno())

    ipr1.close()
     with pytest.raises(OSError) as e:
        ipr2.get_links()
     assert e.value.errno == 9  # sendto -> Bad file descriptor
 
    with pytest.raises(OSError) as e:
        ipr2.close()
    assert e.value.errno == 9  # close -> Bad file descriptor

 
 def test_get_policy_map(context):
     assert isinstance(context.ipr.get_policy_map(), dict)