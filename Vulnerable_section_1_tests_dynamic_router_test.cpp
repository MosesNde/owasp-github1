     void rot13_path(context& ctx) const {
         auto uri = ctx.request.uri();
         rot13(uri);
        ctx.request.uri(uri); // set the uri again
     }
     // NOLINTEND(readability-convert-member-functions-to-static)
 };
     req.method("GET");
     req.uri("/page/about");
     EXPECT_EQ(req.uri(), "/page/about");
    auto it = req.path_iterator();
    EXPECT_TRUE(it.check_segment("page")) << *it;
    EXPECT_TRUE(it.check_segment("about")) << *it;
 
     auto res = router(req);
     EXPECT_EQ(res.headers.status_code(), status_code::ok) << router.to_string();
     EXPECT_NE(as<std::string>(res.body), "about page");
 }
 
 TEST(DynamicRouter, CommonBypassTests) {
     enable_traits_for<dynamic_router> router;
     router.objects.emplace_back(pages{});
     request req{router.get_traits()};
     req.method("GET");
 
    for (auto const u : {"/%2e/admin",
                         "/admin/.",
                         "//admin//",
                         "/./admin/..",
                         "/;/admin",
                         "/.;/admin",
                         "//;//admin",
                         "/admin..;/",
                         "/aDmIN"}) {
        req.uri(u);
         auto const res = router(req);
         EXPECT_EQ(res.headers.status_code(), status_code::not_found)
           << res.headers.status_code_integer() << "\n"
           << router.to_string() << "\n"
          << u;
        EXPECT_NE(as<std::string>(res.body), "about page") << u;
     }
 }
 
 
     auto const res = router(req);
     EXPECT_EQ(res.headers.status_code(), status_code::ok) << router.to_string();
    EXPECT_EQ(as<std::string>(res.body), "about page");
 }
 
 TEST(DynamicRouter, SameOrderPreRoutingTest) {
         EXPECT_FALSE(ctx.path_traverser().at_end()) << num;
         // rot13 should already be run, so we should get a clear "page" as the first segment
         EXPECT_EQ("page", ctx.path_traverser().peek().value_or(""))
           << "Segment: " << *ctx.path_traverser() << "\n"
           << "Should be called before checking the paths, it's a pre-routing.\nNum: " << num
          << "\nRouter: " << router.to_string();
         ++num;
     };
 
 
 
 TEST(DynamicRouter, ContextCurrentRoute) {
    enable_owner_traits<default_dynamic_traits> et;
 
    dynamic_router router{et};
     router += root / "home" >> [](context& ctx) {
         return ctx.current_route().to_string();
     };
 
    request req{et};
     req.method("GET");
     req.uri("/home");
 
     HTTPResponse auto const res = router(req);
     EXPECT_EQ(res.headers.status_code(), status_code::ok);
    EXPECT_TRUE(as<std::string>(res.body).find("/home") != std::string::npos) << as<std::string>(res.body);
 }
 
 