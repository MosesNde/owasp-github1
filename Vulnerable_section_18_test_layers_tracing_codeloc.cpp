  *
  */
 
 #include <gtest/gtest.h>
 #include <ur_api.h>
 
 }
 
 TEST(LoaderCodeloc, NullCallback) {
    ur_loader_config_handle_t loader_config;
    ASSERT_EQ(urLoaderConfigCreate(&loader_config), UR_RESULT_SUCCESS);
     ASSERT_EQ(
         urLoaderConfigSetCodeLocationCallback(loader_config, nullptr, nullptr),
         UR_RESULT_ERROR_INVALID_NULL_POINTER);
    urLoaderConfigRelease(loader_config);
 }
 
 TEST(LoaderCodeloc, NullHandle) {
 }
 
 TEST(LoaderCodeloc, Success) {
    ur_loader_config_handle_t loader_config;
    ASSERT_EQ(urLoaderConfigCreate(&loader_config), UR_RESULT_SUCCESS);
     ASSERT_EQ(urLoaderConfigSetCodeLocationCallback(loader_config,
                                                     test_callback, nullptr),
               UR_RESULT_SUCCESS);
     urLoaderInit(0, loader_config);
     uint32_t nadapters;
     urAdapterGet(0, nullptr, &nadapters);
    urLoaderConfigRelease(loader_config);
 }