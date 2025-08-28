 # -*- coding: utf-8 -*-
 from datetime import datetime, timedelta
 from elasticsearch_dsl import Search
 from elasticsearch import Elasticsearch
 from random import choice
 from sefaria.utils.hebrew import hebrew_term, has_hebrew
 from sefaria.utils.calendars import get_all_calendar_items, get_todays_calendar_items, get_keyed_calendar_items, get_parasha, get_todays_parasha
 from sefaria.settings import STATIC_URL, USE_VARNISH, USE_NODE, NODE_HOST, DOMAIN_LANGUAGES, MULTISERVER_ENABLED, MULTISERVER_REDIS_SERVER, \
    MULTISERVER_REDIS_PORT, MULTISERVER_REDIS_DB, DISABLE_AUTOCOMPLETER, ENABLE_LINKER
 from sefaria.site.site_settings import SITE_SETTINGS
 from sefaria.system.multiserver.coordinator import server_coordinator
 from sefaria.system.decorators import catch_error_as_json, sanitize_get_params, json_response_decorator
     Set the interfaceLang cookie, saves to UserProfile (if logged in)
     and redirects to `next` url param.
     """
    next = request.GET.get("next", "/")
    next = "/" if next == "undefined" else next
 
     for domain in DOMAIN_LANGUAGES:
         if DOMAIN_LANGUAGES[domain] == language and not request.get_host() in domain: