     do {
         ssize_t n = read(f, ent32 + have, NUM_OS_RANDOM_BYTES - have);
         if (n <= 0 || n + have > NUM_OS_RANDOM_BYTES) {
             RandFailure();
         }
         have += n;