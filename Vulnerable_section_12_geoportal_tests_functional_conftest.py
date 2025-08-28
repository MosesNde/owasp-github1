 from unittest.mock import patch
 
 import pytest
 from c2c.template.config import config as configuration
 from pyramid.testing import DummyRequest
 from tests.functional import setup_common as setup_module
 
 
 @pytest.fixture
 def settings():
     request.dbsession = dbsession
 
     return request