         }
 
         if (setns(fd, CLONE_NEWNS) != 0) {
             return false;
         }
 
         char *stackTop = stack + stackSize;
         pid_t pid = clone(ChildFunc, stackTop, flag | SIGCHLD, nullptr);
         if (pid == -1) {
             return false;
         }
         return true;