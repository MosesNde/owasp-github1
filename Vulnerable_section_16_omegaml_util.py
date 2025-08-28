 from __future__ import absolute_import
 
import pathlib

from pathlib import Path

from copy import deepcopy
 from importlib import import_module
 
 import json
 import sys
 import tempfile
 import uuid
 import warnings
 from base64 import b64encode
 from bson import UuidRepresentation
 from datetime import datetime
 from shutil import rmtree
 
 try:
     _omega = None
 
     def load_customized():
        mod = import_module(os.environ.get('OMEGA_CUSTOM_LOADER', ''))
         _omega = mod.omega
         _base_config_client = mod.defaults
         _base_config.update_from_obj(_base_config_client, attrs=_base_config)
     def __missing__(self, key):
         return '{' + key + '}'
 