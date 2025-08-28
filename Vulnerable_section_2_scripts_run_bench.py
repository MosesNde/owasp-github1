 
 def get_git_hash():
     """ Get hash of the current git HEAD. """
    return subprocess.check_output("git rev-parse HEAD", shell=True)
 
 
 def get_git_branch():
     """ Get the current git branch. """
    return subprocess.check_output("git rev-parse --abbrev-ref HEAD",
                                   shell=True).strip()
 
 
 def run(program_name, num_run):