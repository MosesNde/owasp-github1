 # See the Mulan PSL v2 for more details.
 # ******************************************************************************/
 import os
 from typing import Optional, Tuple
 
 from ceres.conf.constant import CommandExitCode, CveFixTaskType, TaskExecuteRes
         Returns:
             Tuple[str, str]: a tuple containing two elements (rollback result, log)
         """
        cmd = f"dnf history rollback {dnf_event_start} -y"
         # 'dnf history rollback transaction-id' command can revert all dnf transactions performed after transaction-id
         code, stdout, stderr = execute_shell_command(cmd)
         if code != CommandExitCode.SUCCEED:
         Returns:
             Tuple[str, str]: a tuple containing two elements (remove result, log)
         """
        code, stdout, stderr = execute_shell_command(f"rpm -qa | grep {installed_rpm}")
         # 'rpm -qa' shows installed rpm
         # e.g.
         # [root@openEuler ~]# rpm -qa | grep kernel-4.19.90-2112.8.0.0131.oe1.x86_64
             LOGGER.error(tmp_log)
             return TaskExecuteRes.FAIL, tmp_log
         
        code, current_evra, stderr = execute_shell_command(f"uname -r")
        # 'uname -r' show the kernel version-release.arch of the current system
        # e.g.
        # [root@openEuler ~]# uname -r
        # 5.10.0-136.12.0.86.oe2203sp1.x86_64
        if code != CommandExitCode.SUCCEED:
            LOGGER.error(stderr)
            return TaskExecuteRes.FAIL, current_evra + stderr
         
         # version-release.arch
         installed_evra = installed_rpm.split("-", 1)[1]
         
         if installed_evra == current_evra:
             return TaskExecuteRes.SUCCEED, f"Preserve the {installed_rpm} due to it is in use."
         
        code, stdout, stderr = execute_shell_command(f"dnf remove {installed_rpm} -y")
         if code != CommandExitCode.SUCCEED:
             LOGGER.error(stderr)
             return TaskExecuteRes.FAIL, stdout + stderr
         Returns:
             Tuple[str, str]: a tuple containing two elements (check result, log)
         """
        code, stdout, stderr = execute_shell_command(f"grubby --default-kernel")
         # 'grubby --default-kernel' shows boot default kernel version in the system
         # e.g.
         # [root@openEuler ~]# grubby --default-kernel
         Returns:
             Tuple[str, str]: a tuple containing two elements (check result, log)
         """
        code, current_evra, stderr = execute_shell_command(f"uname -r")
        # 'uname -r' show the kernel version-release.arch of the current system
        # e.g.
        # [root@openEuler ~]# uname -r
        # 5.10.0-136.12.0.86.oe2203sp1.x86_64
        if code != CommandExitCode.SUCCEED:
            LOGGER.error(stderr)
            return TaskExecuteRes.FAIL, current_evra + stderr
 
         installed_evra = installed_rpm.split("-", 1)[1]
         target_evra = target_rpm.split("-", 1)[1]
 
     def _check_if_target_rpm_installed(self, target_rpm: str) -> Tuple[str, str]:
         """
        Check if the target kernel is installed. If not, it indicates that the environment after executed fix 
         task has been tampered.
 
         Args:
         Returns:
             Tuple[str, str]: a tuple containing two elements (check result, log)
         """
        code, stdout, stderr = execute_shell_command(f"rpm -qa | grep {target_rpm}")
         # 'rpm -qa' shows installed rpm
         # e.g.
         # [root@openEuler ~]# rpm -qa | grep kernel-4.19.90-2112.8.0.0131.oe1.x86_64
             return TaskExecuteRes.FAIL, tmp_log
 
         # 'grubby --set-default=/boot/vmlinuz-xxx' changes the default boot entry
        code, stdout, stderr = execute_shell_command(f"grubby --set-default={boot_file}")
         if code != CommandExitCode.SUCCEED:
             LOGGER.error(stderr)
             return TaskExecuteRes.FAIL, stdout + stderr