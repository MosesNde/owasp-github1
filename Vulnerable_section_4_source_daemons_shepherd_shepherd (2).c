             shepherd_trace("calling fork_no_pty()");
             pid = fork_no_pty(fd_pipe_in, fd_pipe_out, fd_pipe_err, &err_msg);
          }
      } 
 
       if (pid==0)
       {
       {
          /* received any other signal */
 #if defined(INTERIX)
         sge_set_environment();
          if (strcmp(childname, "job") == 0 &&
              wl_get_GUI_mode(get_conf_val("display_win_gui")) == true)
          {
 
 #if defined(INTERIX)
       /* <Windows_GUI> */
      sge_set_environment();
       if (strcmp(childname, "job") == 0 &&
          wl_get_GUI_mode(get_conf_val("display_win_gui")) == true) {
          if (npid != -1) {      
       pid = getpid();
       setpgid(pid, pid);  
       setrlimits(0);
      sge_set_environment();
       umask(022);
 
       tmp_str = search_conf_val("qsub_gid");
       if (!strcmp(name, "PVM_TASK_ID"))
          strcpy(pvm_task_id, value);
 
       sge_set_env_value(name, value);
    }
 