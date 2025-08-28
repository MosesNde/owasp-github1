 #include "path/to/httplib.h"
 
 // HTTP
httplib::Client cli("http://cpp-httplib-server.yhirose.repl.co");
 
 // HTTPS
httplib::Client cli("https://cpp-httplib-server.yhirose.repl.co");
 
 auto res = cli.Get("/hi");
 res->status;
 
 // Disable cert verification
 cli.enable_server_certificate_verification(false);
 ```
 
 > [!NOTE]
     res.set_content(req.body, "text/plain");
   });
 
   svr.Get("/stop", [&](const Request& req, Response& res) {
     svr.stop();
   });
 });
 ```
 
 ### 'Expect: 100-continue' handler
 
 By default, the server sends a `100 Continue` response for an `Expect: 100-continue` header.
 
 ### Default thread pool support
 
`ThreadPool` is used as a **default** task queue, and the default thread count is 8, or `std::thread::hardware_concurrency()`. You can change it with `CPPHTTPLIB_THREAD_POOL_COUNT`.
 
 If you want to set the thread count at runtime, there is no convenient way... But here is how.
 
 
 ```c++
 httplib::Headers headers = {
  { "Accept-Encoding", "gzip, deflate" }
 };
 auto res = cli.Get("/hi", headers);
 ```
 or
 ```c++
auto res = cli.Get("/hi", {{"Accept-Encoding", "gzip, deflate"}});
 ```
 or
 ```c++
 cli.set_default_headers({
  { "Accept-Encoding", "gzip, deflate" }
 });
 auto res = cli.Get("/hi");
 ```
 cli.set_connection_timeout(0, 300000); // 300 milliseconds
 cli.set_read_timeout(5, 0); // 5 seconds
 cli.set_write_timeout(5, 0); // 5 seconds
 ```
 
 ### Receive content with a content receiver
 Brotli compression is available with `CPPHTTPLIB_BROTLI_SUPPORT`. Necessary libraries should be linked.
 Please see https://github.com/google/brotli for more detail.
 
 ### Compress request body on client
 
 ```c++
 
 ```c++
 cli.set_decompress(false);
res = cli.Get("/resource/foo", {{"Accept-Encoding", "gzip, deflate, br"}});
 res->body; // Compressed data
 ```
 
Use `poll` instead of `select`
-------------------------------
 
`select` system call is used as default since it's more widely supported. If you want to let cpp-httplib use `poll` instead, you can do so with `CPPHTTPLIB_USE_POLL`.
 
 
 Split httplib.h into .h and .cc
 Wrote out/httplib.h and out/httplib.cc
 ```
 
 NOTE
 ----
 
 > cpp-httplib officially supports only the latest Visual Studio. It might work with former versions of Visual Studio, but I can no longer verify it. Pull requests are always welcome for the older versions of Visual Studio unless they break the C++11 conformance.
 
 > [!NOTE]
> Windows 8 or lower, Visual Studio 2013 or lower, and Cygwin and MSYS2 including MinGW are neither supported nor tested.
 
 License
 -------
 
MIT license (© 2024 Yuji Hirose)
 
 Special Thanks To
 -----------------