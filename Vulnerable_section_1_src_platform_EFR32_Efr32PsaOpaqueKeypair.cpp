 
 EFR32OpaqueKeypair::~EFR32OpaqueKeypair()
 {
    // Free dynamic resource
     if (mContext != nullptr)
     {
         MemoryFree(mContext);
         mContext = nullptr;
     }
 
     // Store the key ID and mark the key as valid
     mHasKey       = true;
    mIsPersistent = key_id != kEFR32OpaqueKeyIdVolatile;
 
 exit:
     psa_reset_key_attributes(&attr);