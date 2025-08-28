         Returns:
             str:The memory value which has used
         """
        code, stdout, _ = execute_shell_command(f"cat /proc/{pid}/status|grep VmRSS")
         if code == CommandExitCode.SUCCEED:
             return stdout.split(":")[1].strip()
         LOGGER.error(f'Failed to get memory info of process {pid}!')
         Returns:
             str: cpu usage
         """
        code, stdout, _ = execute_shell_command(f"ps -aux|grep -w {rpm_name}|grep {pid}|awk {{print$3}}")
         if code == CommandExitCode.SUCCEED:
             return f'{stdout.strip()}%'
         LOGGER.error(f'Failed to get plugin cpu info about {rpm_name}.')