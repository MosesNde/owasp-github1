 """
 
 from typing import Text, List
 
 from oic.oic.message import AuthorizationRequest as OICAuthRequest
 
 from .oidc.authorize import validate_jwt_token
 
 from .cache import RedisCache
 from .models import AuthorizeRequest
from .exceptions import ExpiredResourceError
 
 from . import constants
 
 
def create_redis_bsn_key(key: str, id_token: str, audience: List[Text]) -> str:
     """
     Method retrieving the redis_bsn_key used to retrieve the bsn from redis. This is the hash of the id_token that has
     been provided as a response to the accesstoken request.
     """
     result = redis_cache.hget(namespace, key)
     if result is None:
        raise ExpiredResourceError("Resource is not (any longer) available in redis")
     return result