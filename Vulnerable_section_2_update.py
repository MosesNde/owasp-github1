     if error:
         exit(1)
 
     # 1. Update the service
     # ---------------------
 
         print("Failed: Could not update the service '%s'! (Error %i)" % (service, update.status_code))
         exit(6)
 
     print('Success!')
 
 