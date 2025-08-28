     ('//evil.com:80', False),
     ('http://evil.com', False),
     ('https://evil.com', False),
     ('javascript:alert("eeeeeeeevil")', False),
 ))
 def test_validate_next_url(url, valid):