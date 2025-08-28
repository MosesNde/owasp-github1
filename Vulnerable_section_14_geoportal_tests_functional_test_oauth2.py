             "type": "oauth2",
         }
         request.method = "POST"
         request.body = ""
         with pytest.raises(pyramid.httpexceptions.HTTPFound) as exc_info:
             Login(request).login()
             "grant_type": "authorization_code",
             "redirect_uri": "http://127.0.0.1:7070/",
         }
         request.body = urllib.parse.urlencode(request.POST)
         request.method = "POST"
         response = Login(request).oauth2token()
             "response_type": "code",
             "type": "oauth2",
         }
         request.method = "POST"
         request.body = ""
         with pytest.raises(pyramid.httpexceptions.HTTPFound) as exc_info:
             "grant_type": "authorization_code",
             "redirect_uri": "http://127.0.0.1:7070/",
         }
         request.body = urllib.parse.urlencode(request.POST)
         request.method = "POST"
         with pytest.raises(pyramid.httpexceptions.HTTPUnauthorized):
             "grant_type": "authorization_code",
             "redirect_uri": "http://127.0.0.1:7070/",
         }
         request.body = urllib.parse.urlencode(request.POST)
         request.method = "POST"
         with pytest.raises(pyramid.httpexceptions.HTTPBadRequest):
             "response_type": "code",
             "type": "oauth2",
         }
         request.method = "POST"
         request.body = ""
         with pytest.raises(pyramid.httpexceptions.HTTPFound) as exc_info:
             "grant_type": "authorization_code",
             "redirect_uri": "http://127.0.0.1:7070/",
         }
         request.body = urllib.parse.urlencode(request.POST)
         request.method = "POST"
         response = Login(request).oauth2token()
             "response_type": "code",
             "type": "oauth2",
         }
         request.method = "POST"
         request.body = ""
         with pytest.raises(pyramid.httpexceptions.HTTPFound) as exc_info:
             "grant_type": "authorization_code",
             "redirect_uri": "http://127.0.0.1:7070/",
         }
         request.body = urllib.parse.urlencode(request.POST)
         request.method = "POST"
         response = Login(request).oauth2token()
             "response_type": "code",
             "type": "oauth2",
         }
         request.method = "POST"
         request.body = ""
         with pytest.raises(pyramid.httpexceptions.HTTPFound) as exc_info:
             "grant_type": "authorization_code",
             "redirect_uri": "http://127.0.0.1:7070/",
         }
         request.body = urllib.parse.urlencode(request.POST)
         request.method = "POST"
         with pytest.raises(pyramid.httpexceptions.HTTPBadRequest):
             "response_type": "code",
             "type": "oauth2",
         }
         request.method = "POST"
         request.body = ""
         with pytest.raises(pyramid.httpexceptions.HTTPFound) as exc_info:
             "grant_type": "authorization_code",
             "redirect_uri": "http://127.0.0.1:7070/",
         }
         request.body = urllib.parse.urlencode(request.POST)
         request.method = "POST"
         response = Login(request).oauth2token()
             "response_type": "code",
             "type": "oauth2",
         }
         request.method = "POST"
         request.body = ""
         pyramid.testing.setUp(request=request, registry=init_registry())
             "code_challenge": code_challenge,
             "code_challenge_method": "S256",
         }
         request.method = "POST"
         request.body = ""
         with pytest.raises(pyramid.httpexceptions.HTTPFound) as exc_info:
             "grant_type": "authorization_code",
             "redirect_uri": "http://127.0.0.1:7070/",
         }
         request.body = urllib.parse.urlencode(request.POST)
         request.method = "POST"
         response = Login(request).oauth2token()
             "code_challenge": code_challenge,
             "code_challenge_method": "S256",
         }
         request.method = "POST"
         request.body = ""
         with pytest.raises(pyramid.httpexceptions.HTTPFound) as exc_info:
             "grant_type": "authorization_code",
             "redirect_uri": "http://127.0.0.1:7070/",
         }
         request.body = urllib.parse.urlencode(request.POST)
         request.method = "POST"
         response = Login(request).oauth2token()
             "response_type": "code",
             "type": "oauth2",
         }
         request.method = "POST"
         request.body = ""
         with pytest.raises(pyramid.httpexceptions.HTTPBadRequest) as exc_info:
             "response_type": "code",
             "type": "oauth2",
         }
         request.method = "POST"
         request.body = ""
         with pytest.raises(pyramid.httpexceptions.HTTPFound) as exc_info:
             "code_challenge": code_challenge,
             "code_challenge_method": "S256",
         }
         request.method = "POST"
         request.body = ""
         with pytest.raises(pyramid.httpexceptions.HTTPBadRequest) as exc_info:
             "code_challenge": code_challenge,
             "code_challenge_method": "S256",
         }
         request.method = "POST"
         request.body = ""
         with pytest.raises(pyramid.httpexceptions.HTTPFound) as exc_info:
             "grant_type": "authorization_code",
             "redirect_uri": "http://127.0.0.1:7070/",
         }
         request.body = urllib.parse.urlencode(request.POST)
         request.method = "POST"
         with pytest.raises(pyramid.httpexceptions.HTTPBadRequest) as exc_info: