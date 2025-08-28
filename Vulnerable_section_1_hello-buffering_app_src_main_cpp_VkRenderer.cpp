     for (auto uniformMemory : mUniformMemories) {
         vkUnmapMemory(mDevice, uniformMemory);
     }
    mUniformMemories.clear();
     for (auto uniformMemory : mUniformMemories) {
         vkFreeMemory(mDevice, uniformMemory, nullptr);
     }