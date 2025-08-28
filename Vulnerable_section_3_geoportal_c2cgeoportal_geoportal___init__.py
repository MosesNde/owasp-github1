 import importlib
 import logging
 import os
 from functools import partial
 from typing import TYPE_CHECKING, Any, Callable, Optional, cast
from urllib.parse import urlsplit
 
 import c2cgeoform
 import c2cwsgiutils
 from papyrus.renderers import GeoJSON
 from prometheus_client.core import REGISTRY
 from pyramid.config import Configurator
from pyramid.httpexceptions import HTTPException
 from pyramid.path import AssetResolver
 from pyramid_mako import add_mako_renderer
 from sqlalchemy.orm import Session, joinedload
     return reference_parts == value_parts
 
 
 def is_valid_referrer(request: pyramid.request.Request, settings: Optional[dict[str, Any]] = None) -> bool:
     """Check if the referrer is valid."""
     if request.referrer is not None:
        referrer = urlsplit(request.referrer)._replace(query="", fragment="").geturl().rstrip("/").split("/")
         if settings is None:
             settings = request.registry.settings
        list_ = settings.get("authorized_referers", [])
        return any(_match_url_start(e, referrer) for e in list_)
     return True
 
 