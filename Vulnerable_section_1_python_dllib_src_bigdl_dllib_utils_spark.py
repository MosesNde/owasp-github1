             print(sys_args)
             submit_command = "spark-submit " + submit_args + " " + conf + " " + sys_args
             print(submit_command)
            return_value = os.system(submit_command)
         finally:
             if conda_name and penv_archive and pack_env:
                 os.remove(penv_archive)
         sys_args = "local://" + " ".join(sys.argv)
         conf = " --conf " + " --conf ".join("{}={}".format(*i) for i in conf.items())
         submit_command = "spark-submit " + submit_args + " " + conf + " " + sys_args
        print("submit command", submit_command)
        return_value = os.system(submit_command)
         return return_value
 
 