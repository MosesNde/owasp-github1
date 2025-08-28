         cursor = connection.cursor()
         cursor.execute(query)
         row = cursor.fetchone()
        # This allows SQL injection, use this instead
        # user = authenticate(request, username=username, password=password)

         if row:
             user = User.objects.get(username=username)
            login(request, user)  # actually log the user in
             return redirect("home")
         else:
             return HttpResponse("Invalid credentials")
 
     return render(request, "login.html")
 