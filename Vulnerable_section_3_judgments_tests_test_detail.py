 
 import pytest
 from caselawclient.errors import JudgmentNotFoundError
from django.http import Http404
 from django.test import TestCase
 from factories import JudgmentFactory
 
         mock_head.assert_called_with(
             "http://example.com/test.pdf", headers={"Accept-Encoding": None}
         )