 import os
 import shlex
 import subprocess
from typing import Union, Tuple, NoReturn
 
 from libconf import load, ConfigParseError, AttrDict
 from jsonschema import validate, ValidationError
         return False, {}
 
 
def execute_shell_command(command: str, **kwargs) -> Tuple[int, str, str]:
     """
     execute shell commands
 
     Args:
        command(str): shell command which needs to execute
         **kwargs: keyword arguments, it is used to create Popen object.supported options: env, cwd, bufsize, group and
         so on. you can see more options information in annotation of Popen obejct.
 
         a tuple containing three elements (return code, standard output, standard error).
 
     Example usage:
    >>> return_code, stdout, stderr = execute_shell_command("ls -al|wc -l", **{"env": {"LANG": "en_US.utf-8"}})
     >>> print(return_code, stdout, stderr)
     0, 42, ""
     """
    commands = command.split('|')
     process = None
     stdout_data = ""
     stderr_data = ""
                     stderr=subprocess.PIPE,
                     stdin=subprocess.PIPE,
                     encoding='utf-8',
                     **kwargs,
                 )
             else:
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE,
                     encoding='utf-8',
                     **kwargs,
                 )
         stdout, stderr = process.communicate()
     if service_name is None:
         LOGGER.warning(f"Fail to get service name about {plugin_name}")
         return ""
    return_code, stdout, _ = execute_shell_command(f"systemctl status {service_name}|grep Active")
 
     if return_code == CommandExitCode.SUCCEED:
         return stdout