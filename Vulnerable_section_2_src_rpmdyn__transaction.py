 
         assert isinstance(fd, int)
 
        rpmfd = _ffi.fdDup(fd)
 
         h = _ffi.ffi.new("Header*")
         res = _ffi.rpmReadPackageFile(
         # TODO: raise proper exceptions
         assert res == _const.RPMRC_OK
 
        return Header(_ffi.ffi.cast("Header", h[0]))