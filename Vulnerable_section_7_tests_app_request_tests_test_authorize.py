 
     assert response.status_code == 307
     assert response.headers["location"].startswith("/sorry-something-went-wrong")