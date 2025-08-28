 # -*- coding: utf-8 -*-
 from datetime import datetime, timedelta
 from elasticsearch_dsl import Search
 from elasticsearch import Elasticsearch
 from random import choice
 from django.utils.html import strip_tags
 from bson.objectid import ObjectId
 
 from sefaria.model import *
 from sefaria.google_storage_manager import GoogleStorageManager
 from sefaria.model.text_reuqest_adapter import TextRequestAdapter
     Set the interfaceLang cookie, saves to UserProfile (if logged in)
     and redirects to `next` url param.
     """
    next = request.GET.get("next", "/")
    next = "/" if next == "undefined" else next
 
     for domain in DOMAIN_LANGUAGES:
         if DOMAIN_LANGUAGES[domain] == language and not request.get_host() in domain: