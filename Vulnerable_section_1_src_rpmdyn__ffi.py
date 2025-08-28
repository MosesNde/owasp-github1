 ffi.cdef(
     """
     typedef void* Header;
     typedef void* rpm_data_t;
     typedef void* rpmKeyring;
     typedef uint32_t rpm_count_t;
 
     rpmTagReturnType rpmTagGetReturnType(rpmTagVal);
 
    void* fdDup(int);
 
     rpmtd rpmtdNew();
     rpmtd rpmtdFree(void*);
 
 rpmTagGetReturnType = rpm.rpmTagGetReturnType
 fdDup = rpmio.fdDup
 
 rpmtdNew = rpm.rpmtdNew
 rpmtdFree = rpm.rpmtdFree