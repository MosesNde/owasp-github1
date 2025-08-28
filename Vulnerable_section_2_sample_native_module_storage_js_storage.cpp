     napi_get_cb_info(env, info, nullptr, nullptr, &thisVar, &data);
 
     auto objectInfo = new StorageObjectInfo(env);
    napi_wrap(
         env, thisVar, objectInfo,
         [](napi_env env, void* data, void* hint) {
             auto objectInfo = (StorageObjectInfo*)data;
             }
         },
         nullptr, nullptr);
 
     return thisVar;
 }