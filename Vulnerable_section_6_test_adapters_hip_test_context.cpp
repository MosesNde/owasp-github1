 #include "context.hpp"
 #include "fixtures.h"
 #include "queue.hpp"
 
 using urHipContextTest = uur::urDeviceTest;
 UUR_INSTANTIATE_DEVICE_TEST_SUITE_P(urHipContextTest);
 
 TEST_P(urHipContextTest, ActiveContexts) {
    ur_context_handle_t context = nullptr;
    ASSERT_SUCCESS(urContextCreate(1, &device, nullptr, &context));
     ASSERT_NE(context, nullptr);
 
    ur_queue_handle_t queue = nullptr;
    ASSERT_SUCCESS(urQueueCreate(context, device, nullptr, &queue));
     ASSERT_NE(queue, nullptr);
 
     // ensure that the queue has the correct context
     if (context->getDevices().size() == 1) {
         ASSERT_EQ(hipContext, context->getDevices()[0]->getNativeContext());
     }

    ASSERT_SUCCESS(urQueueRelease(queue));
    ASSERT_SUCCESS(urContextRelease(context));
 }
 
 TEST_P(urHipContextTest, ActiveContextsThreads) {
    ur_context_handle_t context1 = nullptr;
    ASSERT_SUCCESS(urContextCreate(1, &device, nullptr, &context1));
     ASSERT_NE(context1, nullptr);
 
    ur_context_handle_t context2 = nullptr;
    ASSERT_SUCCESS(urContextCreate(1, &device, nullptr, &context2));
     ASSERT_NE(context2, nullptr);
 
     // setup synchronization
 
     auto test_thread = std::thread([&] {
         hipCtx_t current = nullptr;
        ur_queue_handle_t queue = nullptr;
        ASSERT_SUCCESS(urQueueCreate(context1, device, nullptr, &queue));
        ASSERT_NE(queue, nullptr);

        // ensure queue has the correct context
        ASSERT_EQ(queue->getContext(), context1);

        // check that the first context is now the active HIP context
        ASSERT_SUCCESS_HIP(hipCtxGetCurrent(&current));
        if (context1->getDevices().size() == 1) {
            ASSERT_EQ(current, context1->getDevices()[0]->getNativeContext());
         }
 
        ASSERT_SUCCESS(urQueueRelease(queue));

         // mark the first set of processing as done and notify the main thread
         {
             std::unique_lock<std::mutex> lock(mtx);
             cv.wait(lock, [&] { return released; });
         }
 
        // create a queue with the 2nd context
        queue = nullptr;
        ASSERT_SUCCESS(urQueueCreate(context2, device, nullptr, &queue));
        ASSERT_NE(queue, nullptr);

        // ensure the queue has the correct context
        ASSERT_EQ(queue->getContext(), context2);

        // check that the second context is now the active HIP context
        ASSERT_SUCCESS_HIP(hipCtxGetCurrent(&current));
        if (context2->getDevices().size() == 1) {
            ASSERT_EQ(current, context2->getDevices()[0]->getNativeContext());
         }

        ASSERT_SUCCESS(urQueueRelease(queue));
     });
 
     // wait for the thread to be done with the first queue
     std::unique_lock<std::mutex> lock(mtx);
     cv.wait(lock, [&] { return thread_done; });
    ASSERT_SUCCESS(urContextRelease(context1));
 
     released = true;
     lock.unlock();
     cv.notify_one();
 
     // wait for thread to finish
     test_thread.join();

    ASSERT_SUCCESS(urContextRelease(context2));
 }
 #pragma GCC diagnostic pop