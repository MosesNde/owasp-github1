         try:
             path = filename[:filename.index("/")]
             filename = path[-1]
            fs.create_file(filename, content, path)
         except:
            fs.create_file(filename, content)
     else:
         print(c.Fore.BLUE + params)
 