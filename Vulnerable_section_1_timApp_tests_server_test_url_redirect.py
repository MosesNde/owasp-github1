         self.get("/test//x///?a=b", expect_status=302, expect_content="/test/x?a=b")
         self.get("/view", expect_status=200)
         self.get("/manage", expect_status=302, expect_content="/view")