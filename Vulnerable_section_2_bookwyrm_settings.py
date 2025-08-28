 with open("VERSION", encoding="utf-8") as f:
     version = f.read()
     version = version.replace("\n", "")
f.close()
 
 VERSION = version
 