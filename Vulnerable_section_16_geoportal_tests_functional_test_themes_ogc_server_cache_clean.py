# Copyright (c) 2022, Camptocamp SA
 # All rights reserved.
 
 # Redistribution and use in source and binary forms, with or without
 import asyncio
 from unittest import TestCase
 
 import pytest
 import responses
 import transaction
             "c2cgeoportal_geoportal.views.theme|do_get_http_cached|http://mapserver:8080/?SERVICE=WFS&VERSION=1.0.0&REQUEST=DescribeFeatureType&ROLE_IDS=0&USER_ID=0",
             "c2cgeoportal_geoportal.views.theme|do_get_http_cached|http://mapserver:8080/?SERVICE=WMS&VERSION=1.1.1&REQUEST=GetCapabilities&ROLE_IDS=0&USER_ID=0",
         }