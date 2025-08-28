 from inge6.saml.utils import get_referred_node
 from inge6.saml.exceptions import UserNotAuthenticated
 
from inge6.exceptions import ExpectedRedisValue
 from inge6 import constants
 from inge6.provider import Provider, _get_bsn_from_art_resp
 from inge6.models import AuthorizeRequest, JWTError, SorryPageRequest
     auth_req = AuthorizeRequest(**authorize_params)
 
     # First three calls no problem
    resp = provider.authorize_endpoint(auth_req, headers, "0.0.0.1")
    assert not (
        "location" in resp.headers
        and resp.headers["location"].startswith("/sorry-something-went-wrong")
    )
    resp = provider.authorize_endpoint(auth_req, headers, "0.0.0.2")
    assert not (
        "location" in resp.headers
        and resp.headers["location"].startswith("/sorry-something-went-wrong")
    )
    resp = provider.authorize_endpoint(auth_req, headers, "0.0.0.3")
    assert not (
        "location" in resp.headers
        and resp.headers["location"].startswith("/sorry-something-went-wrong")
    )
 
     # Fourth is the limit.
    resp = provider.authorize_endpoint(auth_req, headers, "0.0.0.4")
    assert resp.headers["location"].startswith("/sorry-something-went-wrong")
 
 
 def test_authorize_invalid_model():
 
     headers: Headers = Headers({})
     auth_req = AuthorizeRequest(**authorize_params)
    resp = mock_provider.authorize_endpoint(auth_req, headers, "0.0.0.0")
    assert resp.status_code == 303
    assert "error=unauthorized_client" in resp.headers["location"]
    assert "error_message=Unknown+client_id" in resp.headers["location"]
    assert f"state={authorize_params['state']}" in resp.headers["location"]
 
 
 # pylint: disable=unused-argument
def test_expected_redis_primary_idp(redis_mock, mock_provider):
     redis_mock.delete(get_settings().primary_idp_key)
 
    authorize_params = {
        "client_id": "some_unknown_client",
        "redirect_uri": "http://localhost:3000/login",
        "response_type": "code",
        "nonce": "n-0S6_WzA2Mj",
        "state": "af0ifjsldkj",
        "scope": "openid",
        "code_challenge": "_1f8tFjAtu6D1Df-GOyDPoMjCJdEvaSWsnqR6SLpzsw",  # code_verifier : SoOEDN-mZKNhw7Mc52VXxyiqTvFB3mod36MwPru253c
        "code_challenge_method": "S256",
    }

     headers: Headers = Headers({})
    auth_req = AuthorizeRequest(**authorize_params)
 
     with pytest.raises(ExpectedRedisValue):
         mock_provider.authorize_endpoint(auth_req, headers, "0.0.0.0")