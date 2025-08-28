 import elasticsearch
 import yaml
 from elasticsearch import Elasticsearch
from flask import current_app, g
 from tinydb import TinyDB, Query, operations
 
 from archivy.config import BaseHooks, Config
 
         return True
     except FileExistsError:
         return False