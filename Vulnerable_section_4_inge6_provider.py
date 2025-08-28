     cache_code_challenge,
     cache_artifact,
     hget_from_redis,
 )
 
 from .encrypt import Encrypt
 from .models import (
    AuthorizeErrorRedirectResponse,
     AuthorizeRequest,
     JWTError,
     JWTResponse,
     LoginDigiDRequest,
     MetaRedirectResponse,
    RateLimitRedirectResponse,
     SAMLAuthNAutoSubmitResponse,
     SomethingWrongHTMLResponse,
     SorryPageRequest,
 )
 
 from .exceptions import (
     DependentServiceOutage,
    TooBusyError,
     TokenSAMLErrorResponse,
    TooManyRequestsFromOrigin,
     ExpiredResourceError,
     UnexpectedAuthnBinding,
     ExpectedRedisValue,
 
     def _get_primary_idp(self, ip_address: str):
         if self._is_outage():
            raise DependentServiceOutage(
                f"Some service we depend on is down according to the redis key: {self.settings.ratelimit.outage_key}"
            )
 
         primary_idp = self.redis_client.get(self.settings.primary_idp_key)
         if primary_idp:
             primary_idp = primary_idp.decode()
         else:
             raise ExpectedRedisValue(
                f"Expected {self.settings.primary_idp_key} key to be set in redis. Please check the primary_idp_key setting"
             )
 
         if (
         Finally, the request is parsed and processed checking the query parameters against the client registration. If all is
         valid, a Redirect response or auto-submit POST response is returned depending on the active IDP and its corresponding configuration.
         """
        try:
            primary_idp = self._get_primary_idp(ip_address)
        except (
            TooBusyError,
            TooManyRequestsFromOrigin,
            DependentServiceOutage,
        ) as rate_limit_error:
            self.log.warning(
                "Rate-limit: Service denied someone access, cancelling authorization flow. Reason: %s",
                str(rate_limit_error),
            )
            return RateLimitRedirectResponse(
                url="/sorry-something-went-wrong?",
                next_redirect_uri=authorize_request.redirect_uri,
                client_id=authorize_request.client_id,
                state=authorize_request.state,
            )
        except ExpectedRedisValue as exp_redis:
            raise exp_redis
        except:  # pylint: disable=bare-except
            self.log.error("Some unhandled error appeard", exc_info=True)
            return AuthorizeErrorRedirectResponse(
                url=authorize_request.redirect_uri,
                error="request_not_supported",
                error_description="Some unhandled error in the rate limit tester. Unclear what went wrong",
                state=authorize_request.state,
                status_code=303,
            )
 
         try:
             auth_req = self.parse_authentication_request(
             if error_url:
                 return RedirectResponse(error_url, status_code=303)
 
            return AuthorizeErrorRedirectResponse(
                url=authorize_request.redirect_uri,
                 error="invalid_request_object",
                 error_description=f"Something went wrong: {str(invalid_auth_req)}",
                state=authorize_request.state,
                status_code=303,
            )
         except Exception as exception:  # pylint: disable=broad-except
             self.log.error("Handling error: %s", exception)
             self.log.error("Some unhandled error appeard", exc_info=True)
            return AuthorizeErrorRedirectResponse(
                url=authorize_request.redirect_uri,
                 error="request_not_supported",
                 error_description="Some unhandled error in the rate limit tester. Unclear what went wrong",
                state=authorize_request.state,
                status_code=303,
            )
 
         randstate = self.redis_cache.gen_token()
         cache_auth_req(