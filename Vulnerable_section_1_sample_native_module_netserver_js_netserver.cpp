 
     NetServer* netServer = new NetServer(env, thisVar);
 
    napi_wrap(
         env, thisVar, netServer,
         [](napi_env env, void* data, void* hint) {
             NetServer* netServer = (NetServer*)data;
             delete netServer;
         },
         nullptr, nullptr);
 
     return thisVar;
 }