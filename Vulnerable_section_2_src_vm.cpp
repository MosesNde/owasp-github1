 bool VM::forkAndExec(ARState &state, const char *filePath, const ArrayObject &argvObj,
                      Value &&redirConfig) {
   // setup self pipe
  int selfPipe[2];
   if (pipe(selfPipe) < 0) {
     fatal_perror("pipe creation error");
   }
   const auto procOp = resolveProcOp(state, ForkKind::NONE);
   auto proc = Proc::fork(state, pgid, procOp);
   if (proc.pid() == -1) {
     raiseCmdError(state, argvObj.getValues()[0].asCStr(), EAGAIN);
     return false;
   } else if (proc.pid() == 0) { // child