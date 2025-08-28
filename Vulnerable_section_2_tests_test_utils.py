from typing import List
 from urllib.parse import parse_qs
 
 import pytest
         cases.append([f"https://{domain}/sub", f"https://{domain}/sub"])
         cases.append([domain, None])
         cases.append([f"//{domain}", f"//{domain}"])
     return cases
 
 
 @pytest.mark.parametrize("url,expected", generate_sanitize_url_cases())
def test_sanitize_url(url, expected):
     sanitized = sanitize_next_url(url)
     assert expected == sanitized
 