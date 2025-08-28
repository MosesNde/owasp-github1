 // SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
 
 #include "kernel.hpp"
#include <uur/fixtures.h>
 
 using cudaKernelTest = uur::urQueueTest;
 UUR_INSTANTIATE_DEVICE_TEST_SUITE_P(cudaKernelTest);
 
 TEST_P(cudaKernelTest, CreateProgramAndKernel) {
 
    ur_program_handle_t program = nullptr;
     ASSERT_SUCCESS(urProgramCreateWithBinary(context, device, sizeof(ptxSource),
                                              (const uint8_t *)ptxSource,
                                             nullptr, &program));
     ASSERT_NE(program, nullptr);
     ASSERT_SUCCESS(urProgramBuild(context, program, nullptr));
 
    ur_kernel_handle_t kernel = nullptr;
    ASSERT_SUCCESS(urKernelCreate(program, "_Z8myKernelPi", &kernel));
     ASSERT_NE(kernel, nullptr);

    ASSERT_SUCCESS(urKernelRelease(kernel));
    ASSERT_SUCCESS(urProgramRelease(program));
 }
 
 TEST_P(cudaKernelTest, CreateProgramAndKernelWithMetadata) {
 
     ur_program_properties_t programProps{UR_STRUCTURE_TYPE_PROGRAM_PROPERTIES,
                                          nullptr, 1, &reqdWorkGroupSizeMDProp};
    ur_program_handle_t program = nullptr;
     ASSERT_SUCCESS(urProgramCreateWithBinary(context, device, sizeof(ptxSource),
                                              (const uint8_t *)ptxSource,
                                             &programProps, &program));
     ASSERT_NE(program, nullptr);
 
     ASSERT_SUCCESS(urProgramBuild(context, program, nullptr));
 
    ur_kernel_handle_t kernel = nullptr;
    ASSERT_SUCCESS(urKernelCreate(program, "_Z8myKernelPi", &kernel));
 
     size_t compileWGSize[3] = {0};
     ASSERT_SUCCESS(urKernelGetGroupInfo(
     for (int i = 0; i < 3; i++) {
         ASSERT_EQ(compileWGSize[i], reqdWorkGroupSizeMD[i + 2]);
     }

    ASSERT_SUCCESS(urKernelRelease(kernel));
    ASSERT_SUCCESS(urProgramRelease(program));
 }
 
 TEST_P(cudaKernelTest, URKernelArgumentSimple) {
    ur_program_handle_t program = nullptr;
     ASSERT_SUCCESS(urProgramCreateWithBinary(context, device, sizeof(ptxSource),
                                              (const uint8_t *)ptxSource,
                                             nullptr, &program));
     ASSERT_NE(program, nullptr);
     ASSERT_SUCCESS(urProgramBuild(context, program, nullptr));
 
    ur_kernel_handle_t kernel = nullptr;
    ASSERT_SUCCESS(urKernelCreate(program, "_Z8myKernelPi", &kernel));
     ASSERT_NE(kernel, nullptr);
 
     int number = 10;
 
     int storedValue = *static_cast<const int *>(kernelArgs[0]);
     ASSERT_EQ(storedValue, number);

    ASSERT_SUCCESS(urKernelRelease(kernel));
    ASSERT_SUCCESS(urProgramRelease(program));
 }
 
 TEST_P(cudaKernelTest, URKernelArgumentSetTwice) {
    ur_program_handle_t program = nullptr;
     ASSERT_SUCCESS(urProgramCreateWithBinary(context, device, sizeof(ptxSource),
                                              (const uint8_t *)ptxSource,
                                             nullptr, &program));
     ASSERT_NE(program, nullptr);
     ASSERT_SUCCESS(urProgramBuild(context, program, nullptr));
 
    ur_kernel_handle_t kernel = nullptr;
    ASSERT_SUCCESS(urKernelCreate(program, "_Z8myKernelPi", &kernel));
     ASSERT_NE(kernel, nullptr);
 
     int number = 10;
     ASSERT_EQ(kernelArgs2.size(), 1 + NumberOfImplicitArgsCUDA);
     storedValue = *static_cast<const int *>(kernelArgs2[0]);
     ASSERT_EQ(storedValue, otherNumber);

    ASSERT_SUCCESS(urKernelRelease(kernel));
    ASSERT_SUCCESS(urProgramRelease(program));
 }
 
 TEST_P(cudaKernelTest, URKernelDispatch) {
    ur_program_handle_t program = nullptr;
     ASSERT_SUCCESS(urProgramCreateWithBinary(context, device, sizeof(ptxSource),
                                              (const uint8_t *)ptxSource,
                                             nullptr, &program));
     ASSERT_NE(program, nullptr);
     ASSERT_SUCCESS(urProgramBuild(context, program, nullptr));
 
    ur_kernel_handle_t kernel = nullptr;
    ASSERT_SUCCESS(urKernelCreate(program, "_Z8myKernelPi", &kernel));
     ASSERT_NE(kernel, nullptr);
 
     const size_t memSize = 1024u;
    ur_mem_handle_t buffer = nullptr;
     ASSERT_SUCCESS(urMemBufferCreate(context, UR_MEM_FLAG_READ_WRITE, memSize,
                                     nullptr, &buffer));
     ASSERT_NE(buffer, nullptr);
     ASSERT_SUCCESS(urKernelSetArgMemObj(kernel, 0, nullptr, buffer));
 
                                          globalWorkOffset, globalWorkSize,
                                          localWorkSize, 0, nullptr, nullptr));
     ASSERT_SUCCESS(urQueueFinish(queue));

    ASSERT_SUCCESS(urMemRelease(buffer));
    ASSERT_SUCCESS(urKernelRelease(kernel));
    ASSERT_SUCCESS(urProgramRelease(program));
 }
 
 TEST_P(cudaKernelTest, URKernelDispatchTwo) {
    ur_program_handle_t program = nullptr;
     ASSERT_SUCCESS(urProgramCreateWithBinary(context, device, sizeof(ptxSource),
                                              (const uint8_t *)twoParams,
                                             nullptr, &program));
     ASSERT_NE(program, nullptr);
     ASSERT_SUCCESS(urProgramBuild(context, program, nullptr));
 
    ur_kernel_handle_t kernel = nullptr;
    ASSERT_SUCCESS(urKernelCreate(program, "twoParamKernel", &kernel));
     ASSERT_NE(kernel, nullptr);
 
     const size_t memSize = 1024u;
    ur_mem_handle_t buffer1 = nullptr;
    ur_mem_handle_t buffer2 = nullptr;
     ASSERT_SUCCESS(urMemBufferCreate(context, UR_MEM_FLAG_READ_WRITE, memSize,
                                     nullptr, &buffer1));
     ASSERT_NE(buffer1, nullptr);
     ASSERT_SUCCESS(urMemBufferCreate(context, UR_MEM_FLAG_READ_WRITE, memSize,
                                     nullptr, &buffer2));
     ASSERT_NE(buffer1, nullptr);
     ASSERT_SUCCESS(urKernelSetArgMemObj(kernel, 0, nullptr, buffer1));
     ASSERT_SUCCESS(urKernelSetArgMemObj(kernel, 1, nullptr, buffer2));
                                          globalWorkOffset, globalWorkSize,
                                          localWorkSize, 0, nullptr, nullptr));
     ASSERT_SUCCESS(urQueueFinish(queue));

    ASSERT_SUCCESS(urMemRelease(buffer1));
    ASSERT_SUCCESS(urMemRelease(buffer2));
    ASSERT_SUCCESS(urKernelRelease(kernel));
    ASSERT_SUCCESS(urProgramRelease(program));
 }