 
         if self._slave is not None: # PTY mode
             os.close(self._slave)

        self._proc.stdin.close()
        self._proc.stdout.close()
        self._proc.stderr.close()
 
     def _is_alive_impl(self) -> bool:
         """Check if the process is alive"""