         print("REQUEST" + str(request.data))
         username = request.data.get('username')
         password = request.data.get('password')
        
         user = authenticate(request, username=username, password=password)
         
         if user is not None: