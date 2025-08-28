 #include "uti/sge_arch.h"
 #include "setosjobid.h"
 #include "sge_fileio.h"
 
 #include "msg_common.h"
 
    setrlimits(!strcmp(childname, "job"));
 
    shepherd_trace("setting environment");
   sge_set_environment();
 
   /* Create the "error" and the "exit" status file here.
    * The "exit_status" file indicates that the son is started.
    return;
 }
 
 /****** Shepherd/sge_set_environment() *****************************************
 *  NAME
 *     sge_set_environment () -- Read the environment from the "environment" file
 *     and store it in the appropriate environment, inherited or internal.
 *
 *  SYNOPSIS
*      int sge_set_environment(void)
 *
 *  FUNCTION
 *     This function reads the "environment" file written out by the execd and
 *  NOTES
 *      MT-NOTE: sge_set_environment() is not MT safe
 *******************************************************************************/
int sge_set_environment()
 {
    const char *const filename = "environment";
    FILE *fp;
 
    while (fgets(buf, sizeof(buf), fp))
    {
      char *name, *value;
       const char *new_value;
 
       line++;
          FCLOSE(fp);
          shepherd_error(1, "error reading environment file: line=%d, contents:%s", line, buf);
       }
 
       value = strtok(NULL, "\n");
       if (value == NULL)
    /* Bugfix: Issuezilla 1300
     * Because this fix could break pre-existing installations, it was made
     * optional. */
    if (inherit_env())
    {
       ret = sge_setenv(name, value);