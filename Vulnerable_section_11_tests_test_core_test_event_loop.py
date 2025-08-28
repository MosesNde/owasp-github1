     assert len(ret) == 5
     assert ret[0] == 1
     assert ret[1] > 1
    assert ret[2] == 2
     assert ret[3] is None
     assert ret[4] == 1
     assert diff_event_loops(state) == 0