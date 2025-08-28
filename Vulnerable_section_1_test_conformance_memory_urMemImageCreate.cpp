                                     &image_format, &image_desc, nullptr,
                                     host_ptr_buffer.ptr()));
 
    ur_mem_handle_t image_handle = nullptr;
     ASSERT_SUCCESS(urMemImageCreate(context, getParam(), &image_format,
                                     &image_desc, host_ptr_buffer.ptr(),
                                    &image_handle));
    ASSERT_NE(nullptr, image_handle);
    ASSERT_SUCCESS(urMemRelease(image_handle));
 }
 
 TEST_P(urMemImageCreateWithHostPtrFlagsTest, InvalidHostPtr) {