     ASSERT_EQ(context, queue->getContext());
 
     // create a buffer in the context to set the context as active
    ur_mem_handle_t buffer;
     ASSERT_SUCCESS(urMemBufferCreate(context, UR_MEM_FLAG_READ_WRITE, 1024,
                                     nullptr, &buffer));
 
     // check that context is now the active cuda context
     ASSERT_SUCCESS_CUDA(cuCtxGetCurrent(&current));