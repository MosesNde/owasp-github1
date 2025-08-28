 # Description: default
 # Date: 2023/6/14 16:31
 import os
import subprocess
 
 from ceres.function.log import LOGGER
from ceres.function.status import (
    UNKNOWN_ERROR,
    SUCCESS
)
from ceres.function.util import execute_shell_command
 
 
 class ListFileManage:
             str: status code
         """
         file_list_res = []
         try:
            command = "ls -l " + directory_path + " | awk '{print $9}'"
            _, stdout, _ = execute_shell_command(command)
            file_list = stdout.split("\n")
            for file in file_list:
                if file:
                    file_path_res = os.path.join(directory_path, file)
                    file_list_res.append(file_path_res)
             return SUCCESS, {"resp": file_list_res}
        except Exception as e:
            LOGGER.error("list the pam.d file failed, with msg{}".format(e))
             return UNKNOWN_ERROR, {"resp": list()}