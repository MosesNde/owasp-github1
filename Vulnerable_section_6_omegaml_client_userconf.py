 import json

import warnings

 import os
 import sys
 import yaml
 from urllib3 import Retry
 
 from omegaml.client.auth import AuthenticationEnv
 
 default_key = 'OMEGA_RESTAPI_URL'
 fallback_url = 'https://hub.omegaml.io'
 def ensure_api_url(api_url, defaults, key=default_key, fallback=fallback_url):
     api_url_default = os.environ.get(key) or os.environ.get(default_key) or fallback
     api_url = api_url or getattr(defaults, key, getattr(defaults, default_key, api_url_default))
     return api_url
 
 