 // See LICENSE.TXT
 // SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
 
#include <uur/fixtures.h>
 
 using SamplerCreateParamTy =
     std::tuple<bool, ur_sampler_addressing_mode_t, ur_sampler_filter_mode_t>;
         filter_mode,                    /* filterMode */
     };
 
    ur_sampler_handle_t hSampler = nullptr;
    ASSERT_SUCCESS(urSamplerCreate(context, &sampler_desc, &hSampler));
     ASSERT_NE(hSampler, nullptr);
    EXPECT_SUCCESS(urSamplerRelease(hSampler));
 }
 
 using urSamplerCreateTest = uur::urContextTest;
         UR_SAMPLER_ADDRESSING_MODE_CLAMP, /* addressing mode */
         UR_SAMPLER_FILTER_MODE_LINEAR,    /* filterMode */
     };
    ur_sampler_handle_t hSampler = nullptr;
    ASSERT_EQ_RESULT(urSamplerCreate(nullptr, &sampler_desc, &hSampler),
                      UR_RESULT_ERROR_INVALID_NULL_HANDLE);
 }
 
         UR_SAMPLER_ADDRESSING_MODE_FORCE_UINT32, /* addressing mode */
         UR_SAMPLER_FILTER_MODE_LINEAR,           /* filterMode */
     };
    ur_sampler_handle_t hSampler = nullptr;
    ASSERT_EQ_RESULT(urSamplerCreate(context, &sampler_desc, &hSampler),
                      UR_RESULT_ERROR_INVALID_ENUMERATION);
 }
 TEST_P(urSamplerCreateTest, InvalidEnumerationFilterMode) {
         UR_SAMPLER_ADDRESSING_MODE_CLAMP,    /* addressing mode */
         UR_SAMPLER_FILTER_MODE_FORCE_UINT32, /* filterMode */
     };
    ur_sampler_handle_t hSampler = nullptr;
    ASSERT_EQ_RESULT(urSamplerCreate(context, &sampler_desc, &hSampler),
                      UR_RESULT_ERROR_INVALID_ENUMERATION);
 }