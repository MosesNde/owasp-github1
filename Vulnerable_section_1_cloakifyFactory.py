 import random
 import sys
 
 # Local Python Imports
 import cloakify
 import decloakify
 	print(f"Creating cloaked file using cipher: {cipherPath}")
 
 	try:
		cloakify.Cloakify(sourceFile, os.path.join(".", "ciphers", cipherPath), cloakedFile, password)
 	except:
 		print("")
 		print("!!! Well that didn't go well. Verify that your cipher is in the 'ciphers/' subdirectory.")