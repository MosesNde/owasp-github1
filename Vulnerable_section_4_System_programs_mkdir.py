     if fs.pathExists(params):
         print(c.Fore.RED + "Cannot create directory! Path exists!")
     else:
        fs.makeDirectory(params)
        print(c.Fore.GREEN + "Directory created!")
     
 def help():
     return "Create directories. Usage: mkdir somedir"
\ No newline at end of file