 # -*- coding: utf-8 -*-
 
 import os
 import shlex
 import subprocess
 from threading import Thread
 from xml.dom import pulldom
import warnings
import platform
 
 try:
     import pwd
 
         self._nmap_options = set(options.split())
         if safe_mode and not self._nmap_options.isdisjoint(unsafe_opts):
            raise Exception("unsafe options activated while safe_mode "
                            "is set True")
         self.__nmap_dynamic_options = options
         self.__sudo_run = ""
         self.__nmap_command_line = self.get_command_line()
             self.__nmap_event_callback = event_callback
         else:
             self.__nmap_event_callback = None
        (self.DONE,
         self.READY,
         self.RUNNING,
         self.CANCELLED,
         self.FAILED) = range(5)
         self._run_init()
 
     def _run_init(self):
         split_char = ";" if self.__is_windows else ":"
         program = program + ".exe" if self.__is_windows else program
         for path in os.environ.get("PATH", "").split(split_char):
            if (
                os.path.exists(os.path.join(path, program)) and not
                os.path.isdir(os.path.join(path, program))
            ):
                 return os.path.join(path, program)
         return None
 
                 2,
                 "sudo is not installed or "
                 "could not be found in system path: "
                "cannot run nmap with sudo"
             )
 
         self.__sudo_run = "{0} -u {1}".format(sudo_path, sudo_user)
                 2,
                 "sudo is not installed or "
                 "could not be found in system path: "
                "cannot run nmap with sudo"
             )
 
         self.__sudo_run = "{0} -u {1}".format(sudo_path, sudo_user)
         except OSError:
             self.__state = self.FAILED
             raise EnvironmentError(
                1, "nmap is not installed or could "
                   "not be found in system path"
             )
 
         while self.__nmap_proc.poll() is None:
         :return: True if nmap process is not running anymore.
         """
         return (
            self.state == self.DONE or
            self.state == self.FAILED or
            self.state == self.CANCELLED
         )
 
     def has_failed(self):
             edomdoc = pulldom.parseString(eventdata)
             for xlmnt, xmlnode in edomdoc:
                 if xlmnt is not None and xlmnt == pulldom.START_ELEMENT:
                    if(
                        xmlnode.nodeName == "taskbegin" and
                        xmlnode.attributes.keys()
                     ):
                         xt = xmlnode.attributes
                         taskname = xt["task"].value
                         self.__nmap_tasks[newtask.name] = newtask
                         self.__current_task = newtask.name
                         rval = True
                    elif(
                        xmlnode.nodeName == "taskend" and
                        xmlnode.attributes.keys()
                     ):
                         xt = xmlnode.attributes
                         tname = xt["task"].value
                         self.__nmap_tasks[tname].status = "ended"
                         rval = True
                     elif (
                        xmlnode.nodeName == "taskprogress" and
                        xmlnode.attributes.keys()
                     ):
                         xt = xmlnode.attributes
                         tname = xt["task"].value
                         self.__nmap_tasks[tname].remaining = remaining
                         self.__nmap_tasks[tname].updated = updated
                         rval = True
                    elif(
                        xmlnode.nodeName == "nmaprun" and
                        xmlnode.attributes.keys()
                     ):
                         self.__starttime = xmlnode.attributes["start"].value
                         self.__version = xmlnode.attributes["version"].value
                         rval = True
                    elif(
                        xmlnode.nodeName == "finished" and
                        xmlnode.attributes.keys()
                     ):
                         self.__endtime = xmlnode.attributes["time"].value
                         self.__elapsed = xmlnode.attributes["elapsed"].value
             )
 
     nm = NmapProcess(
        "scanme.nmap.org",
        options="-A",
        event_callback=mycallback
     )
     rc = nm.run()
     if rc == 0:
        print("Scan started at {0} nmap version: {1}".format(
            nm.starttime, nm.version
             )
         )
         print("state: {0} (rc: {1})".format(nm.state, nm.rc))