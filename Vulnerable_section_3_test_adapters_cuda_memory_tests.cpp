 // SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
 
 #include "fixtures.h"
 
 using cudaMemoryTest = uur::urContextTest;
 UUR_INSTANTIATE_DEVICE_TEST_SUITE_P(cudaMemoryTest);
         ASSERT_SUCCESS_CUDA(cuCtxGetCurrent(&current));
     } while (current != nullptr);
 
    ur_mem_handle_t mem;
     ASSERT_SUCCESS(urMemBufferCreate(context, UR_MEM_FLAG_READ_WRITE, memSize,
                                     nullptr, &mem));
     ASSERT_NE(mem, nullptr);

    ASSERT_SUCCESS(urMemRelease(mem));
 }