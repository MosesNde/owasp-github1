         int ret = pthread_create(&g_thread, nullptr, ThreadFunc, forkArg);
         if (ret != 0) {
             printf("Failed to create thread %d \n", errno);
             return -1;
         }
         usleep(100); // 100 wait