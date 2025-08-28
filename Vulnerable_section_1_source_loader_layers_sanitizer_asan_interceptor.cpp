         static auto MemSet =
             (void *(*)(void *, int, size_t))GetMemFunctionPointer("memset");
         if (!MemSet) {
            context.logger.error(
                "Failed to get 'memset' function from libc.so.6");
             return UR_RESULT_ERROR_UNKNOWN;
         }
 