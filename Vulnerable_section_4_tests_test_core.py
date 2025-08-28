         assert multipass._get_next_url() == '/success'
 
 
 def test_login_finished():
     multipass = Multipass()
     with pytest.raises(AssertionError):