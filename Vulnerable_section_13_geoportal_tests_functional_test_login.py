             params={"came_from": "/came_from"}, POST={"login": "__test_user1", "password": "__test_user1"}
         )
         response = Login(request).login()
        assert response.status_int == 302
         assert response.headers["Location"] == "/came_from"
 
         request = self._create_request_obj(POST={"login": "__test_user1", "password": "__test_user1"})
         response = Login(request).login()
        assert response.status_int == 200
         assert json.loads(response.body.decode("utf-8")) == {
             "username": "__test_user1",
             "email": "__test_user1@example.com",
         request = self._create_request_obj(path="/")
         request.user = DBSession.query(User).filter_by(username="__test_user1").one()
         response = Login(request).logout()
        assert response.status_int == 200
         assert response.body.decode("utf-8") == "true"
 
         request = self._create_request_obj(path="/")
         request.route_url = lambda url: "/dummy/route/url"
         request.user = DBSession.query(User).filter_by(username="__test_user1").one()
         response = Login(request).logout()
        assert response.status_int == 200
         assert response.body.decode("utf-8") == "true"
 
     def test_reset_password(self):
 
         request = self._create_request_obj(POST={"login": username, "password": password})
         response = Login(request).login()
        assert response.status_int == 200
         assert json.loads(response.body.decode("utf-8")) == {
             "username": "__test_user1",
             "is_password_changed": False,