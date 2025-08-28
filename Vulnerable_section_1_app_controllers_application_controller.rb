   def authenticate
     auth_settings = Settings.authentication
     return if session[:authenticated] || auth_settings.blank?
    session[:return_to] = request.fullpath
     redirect_to authentication_path(provider: auth_settings.provider, origin: request.fullpath)
   rescue Settingslogic::MissingSetting
   end