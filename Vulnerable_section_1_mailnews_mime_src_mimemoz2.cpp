 
   msd->options->m_prefBranch = do_GetService(NS_PREFSERVICE_CONTRACTID, &rv);
   if (NS_FAILED(rv)) {
     delete msd;
     return nullptr;
   }
   rv = CallCreateInstance(MOZ_TXTTOHTMLCONV_CONTRACTID, &(msd->options->conv));
   if (NS_FAILED(rv)) {
     msd->options->m_prefBranch = nullptr;
     delete msd;
     return nullptr;
   }