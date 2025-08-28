     user.confirmed_email = true
     user.save!
 
     session[:user_id] = user.id
     redirect_to root_url
   end