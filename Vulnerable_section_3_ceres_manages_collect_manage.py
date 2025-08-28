 import os
 import pwd
 import re
 from socket import AF_INET, SOCK_DGRAM, socket
 from typing import Any, Dict, List, Union
 import xml.etree.ElementTree as ET
         Returns:
             str: e.g openEuler 21.09
         """
        _, stdout, _ = execute_shell_command("cat /etc/os-release")
         res = re.search('(?=PRETTY_NAME=).+', stdout)
 
         if res:
         Returns:
             str
         """
        _, stdout, _ = execute_shell_command("dmidecode -t bios")
 
         res = re.search('(?=Version:).+', stdout)
         if res:
         Returns:
             str
         """
        code, stdout, stderr = execute_shell_command("uname -r")

        if code != CommandExitCode.SUCCEED:
            LOGGER.warning('Failed to get current kernel version, please check uname command and try again')
            LOGGER.warning(stderr)
        return stdout
 
     @staticmethod
     def _get_cpu_info() -> Dict[str, str]:
                     "l3_cache": string
                 }
         """
        _, stdout, _ = execute_shell_command("lscpu", **{"env": {"LANG": "en_US.utf-8"}})
 
         info_list = re.findall('.+:.+', stdout)
 
         Returns:
             str: memory size
         """
        _, stdout, _ = execute_shell_command("lsmem")
 
         res = re.search("(?=Total online memory:).+", stdout)
         if res:
         """
         res = {'size': self.__get_total_online_memory() or None, "total": None, "info": []}
 
        code, memory_data, _ = execute_shell_command("dmidecode -t memory")
 
         # dmidecode -t memory
         # e.g
                     }
                 ]
         """
        code, stdout, _ = execute_shell_command("lshw -xml -c disk")
         if code != CommandExitCode.SUCCEED:
             LOGGER.error(stdout)
             return []
         Returns:
             uuid(str)
         """
        code, stdout, _ = execute_shell_command("dmidecode|grep UUID")
         if code == CommandExitCode.SUCCEED:
             return stdout.replace("-", "").split(':')[1].strip()
         return ""
                 }]
         """
 
        code, source_name_info, _ = execute_shell_command("rpm -qi kernel|grep .src.rpm")
         if code != CommandExitCode.SUCCEED:
             LOGGER.error("Failed to query installed packages.")
             return []