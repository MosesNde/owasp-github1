  */
 
 #include "common.hpp"
 
 #include <asm/param.h>
 #include <dlfcn.h>
 }
 
 void *GetMemFunctionPointer(const char *FuncName) {
    void *handle = dlopen(LIBC_SO, RTLD_NOLOAD);
     if (!handle) {
         return nullptr;
     }
    return dlsym(handle, FuncName);
 }
 
 } // namespace ur_sanitizer_layer