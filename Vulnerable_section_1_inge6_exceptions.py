 from oic.oic.message import TokenErrorResponse
 
 
class TooBusyError(RuntimeError):
     pass
 
 
class TooManyRequestsFromOrigin(RuntimeError):
    pass
 
 
class DependentServiceOutage(RuntimeError):
     pass
 
 
class ExpiredResourceError(RuntimeError):
     pass
 
 
class ExpectedRedisValue(RuntimeError):
     pass
 
 