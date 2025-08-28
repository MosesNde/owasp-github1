 from enum import Enum
 
 from jinja2 import Template
 
 from starlette.background import BackgroundTask
 from starlette.datastructures import URL
 from fastapi import Form
 from fastapi.responses import RedirectResponse
 
 from .config import Settings
 from .saml.saml_request import AuthNRequest
 from .constants import ROOT_DIR
         ] += f"?error={error}&error_description={error_description}&state={state}"
 
 
class RateLimitRedirectResponse(RedirectResponse):
     def __init__(
         self,
         url: typing.Union[str, URL],