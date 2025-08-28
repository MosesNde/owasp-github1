         ] += f"?error={error}&error_description={error_description}&state={state}"
 
 
class RateLimitRedirectResponse(RedirectResponse):
     def __init__(
         self,
         url: typing.Union[str, URL],