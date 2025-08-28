 from dataclasses import dataclass
 from urllib.parse import urlparse
 from hashlib import md5
from time import time
 import requests
 import json
 import asyncio
 import os
 import sys
 from functools import lru_cache
 import cachetools
 
ttl_cache = cachetools.TTLCache(maxsize=2048, ttl=31 * 24 * 60 * 60)
 
 
 app = Flask(__name__)
         _templates_list[temp["id"]] = MemeTemplate(img_url, name, temp["lines"], ext)
     return _templates_list
 
 
 
 @app.route('/', methods=["GET"])
 
 @app.route('/shorten', methods=["GET"])
 def shorten():
     global ttl_cache
     p = request.args.get("path")
    tag = md5((str(time()) + p).encode()).hexdigest()
    ttl_cache[tag] = p
    return flask_json.dumps({'path': p, 'tag': tag})
 
 @app.route('/meme/<string:tag>', methods=["GET"])
 def short_redirect(tag):