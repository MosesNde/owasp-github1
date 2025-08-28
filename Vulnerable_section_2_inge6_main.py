 
 import os.path
 import logging
 
 import uvicorn
 
 from fastapi import FastAPI, Request
 
 from .config import get_settings
 from .router import router
 from .provider import Provider
 
 PROVIDER = Provider()
 
 
 def _validate_saml_identity_provider_settings():
     missing_files = []