         pos++;
         p = buf + pos;
     }
    
     if (pos >= len) {
         return NULL;
     }
 
     sys_file[0] = 0;
     (void)snprintf(sys_file, PATH_LEN, "/sys/block/%s/dev", dev_name);
     if (access(sys_file, 0)) {
         sys_file[0] = 0;
         (void)snprintf(sys_file, PATH_LEN, "/sys/block/*/%s/../dev", dev_name);