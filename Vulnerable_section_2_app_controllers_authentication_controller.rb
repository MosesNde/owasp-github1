 
     return render 'failed', layout: false if auth.blank?
 
    sign_in_github(auth)
 
     if Settings.authentication.blank?
       return redirect_to return_url
     end
 
    session[:authenticated] = true if auth['provider'] == Settings.authentication.provider
 
     redirect_to return_url
   end
     return unless auth[:provider] == 'github'
 
     user = Shipit.github_api.user(auth[:info][:nickname])
    session[:user_id] = User.find_or_create_from_github(user).id
   end
 end