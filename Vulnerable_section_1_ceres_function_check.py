 # PURPOSE.
 # See the Mulan PSL v2 for more details.
 # ******************************************************************************/
 from typing import List, Tuple
 
 from ceres.conf.constant import CommandExitCode
         """
         # Example of command execution result::
         # /boot/vmlinuz-5.10.0-60.18.0.50.oe2203.x86_64
        code, boot_kernel_version, stderr = execute_shell_command("grubby --default-kernel")
         if code != CommandExitCode.SUCCEED:
             LOGGER.error(stderr)
             return False, "Query boot kernel info failed!"
 
        # Example of command execution result::
        # 5.10.0-60.18.0.50.oe2203.x86_64
        code, current_kernel_version, stderr = execute_shell_command("uname -r")
        if code != CommandExitCode.SUCCEED:
            LOGGER.error(stderr)
             return False, "Query current kernel info failed!"
 
         if boot_kernel_version[14:] == current_kernel_version: