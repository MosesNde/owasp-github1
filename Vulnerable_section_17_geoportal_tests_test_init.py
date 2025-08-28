 from unittest import TestCase
 from unittest.mock import patch
 
 from c2c.template.config import config
 from pyramid import testing
 from tests import DummyRequest
         assert self.config.registry.validate_user == custom_validator
 
 
 class TestReferer(TestCase):
     """
     Check that accessing something with a bad HTTP referrer is equivalent to a not authenticated query.
     """
 
     BASE1 = "http://example.com/app"
     BASE2 = "http://friend.com/app2"
    SETTINGS = {"authorized_referers": [BASE1, BASE2]}
     USER = "toto"
 
    def _get_user(self, to, ref, method="GET"):
         class MockRequest:
             def __init__(self, to, ref, method):
                 self.path_qs = to
                 self.referrer = ref
                 self.user_ = TestReferer.USER
                 self.method = method

        config._config = {"schema": "main", "schema_static": "main_static", "srid": 21781}
         get_user = create_get_user_from_request(self.SETTINGS)
         return get_user(MockRequest(to=to, ref=ref, method=method))
 
    def test_match_url(self):
        def match(reference, value, expected):
            r = DummyRequest()
            r.referrer = value
            assert is_valid_referrer(r, {"authorized_referers": [reference]}) == expected

        match("http://example.com/app/", "http://example.com/app?k=v", True)
        match("http://example.com/app/", "http://example.com/app?k=v#link", True)
        match("http://example.com/app/", "http://example.com/app#link", True)
        match("http://example.com/app/", "http://example.com/app", True)
        match("http://example.com/app", "http://example.com/app/", True)
        match("http://example.com/app", "http://example.com/app/x/y", True)
        match("http://example.com", "http://example.com/app/x/y", True)
        match("http://example.com", "http://other.com", False)
        match("http://example.com", "https://example.com", False)
        match("http://example.com/app", "http://example.com/", False)
        match("http://example.com", "http://example.com.bad.org/app/x/y", False)

     def test_positive(self):
         assert self._get_user(to=self.BASE1 + "/1", ref=self.BASE1) == self.USER
         assert self._get_user(to=self.BASE1 + "/2", ref=self.BASE1 + "/3") == self.USER