import subprocess, os, signal, threading
 from queue import Queue, Empty
 
def run(cmd):
     """Spawns a process with command CMD, executed in a shell environment in text mode. Returns a Process object. This function is non-blocking.
 
     Parameter
     Returns
     Process
     A Process object that can be queried for execution results, errors, its status, or to write to the underlying stdin."""
    return Process(cmd)
 
 # FIXME: in the future, add more functions that modify Process constructor arguments for e.g. binary mode, non-shell mode, etc
 
 class Process(object):
     """A subprocess that can run continuously and provides non-blocking interactions."""
 
    def __init__(self, cmd):
         """Initialize and start a subprocess.
 
         Paramter
         cmd : str
         A string that will be executed in a shell environment, in text mode."""
         self._proc = None
         self.stderr_log = Queue()
         self.stdout_log = Queue()
         self._cmdstring = cmdstring
         self._proc = subprocess.Popen(self._cmdstring,
                                       text=True,
                                       stdin=subprocess.PIPE,
                                       shell=True,
                                       preexec_fn=os.setsid,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
 
         self._threads_stop = threading.Event()
         t1 = threading.Thread(target=self._reader, args=[self._proc.stdout, self.stdout_log])
         t2 = threading.Thread(target=self._reader, args=[self._proc.stderr, self.stderr_log])
     def _reader(self, stream, q):
         while w := stream.readline():
             q.put(w)
            if self._threads_stop.isSet():
                 return
             
     def write_line(self, w):
             return lines
         return lines
 
     def close(self):
         # since shell=true spawns child processes that may still be running , we have to terminate by sending kill signal to entire process group
        # FIXME: this doesn't work on windows
         if self._proc:
            os.killpg(os.getpgid(self._proc.pid), signal.SIGTERM)
            self._proc = None
 
 