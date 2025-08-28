         if "running" in plugin_status:
             return SUCCESS
 
        code, _, _ = execute_shell_command(f"systemctl start {self.rpm_name}")
         if code != CommandExitCode.SUCCEED:
             return FAIL
         return SUCCESS
         if "inactive" in plugin_status:
             return SUCCESS
 
        code, _, _ = execute_shell_command(f"systemctl stop {self.rpm_name}")
         if code != CommandExitCode.SUCCEED:
             return FAIL
         return SUCCESS
             str: dead or running
 
         """
        code, stdout, _ = execute_shell_command(f"systemctl status {self.rpm_name}|grep Active")
         if code == CommandExitCode.SUCCEED:
             return re.search(r':.+\(', stdout).group()[1:-1].strip()
         LOGGER.error(f'Failed to get service {self.rpm_name} status!')
         Returns:
             The str type of main process id
         """
        code, main_pid_info, _ = execute_shell_command(f"systemctl status {rpm_name}|grep Main")
         if code == CommandExitCode.SUCCEED:
             return re.search("[0-9]+[0-9]", main_pid_info).group()
         LOGGER.error(f"Failed to get {rpm_name} pid")