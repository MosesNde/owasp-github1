           after_persisting :update_session, :unless => :single_access?
         end
       end
      
       # Configuration for the session feature.
       module Config
         # Works exactly like cookie_key, but for sessions. See cookie_key for more info.
         end
         alias_method :session_key=, :session_key
       end
      
       # Instance methods for the session feature.
       module InstanceMethods
         private
               false
             end
           end
          
           def session_credentials
            [controller.session[session_key], controller.session["#{session_key}_#{klass.primary_key}"]].compact
           end
          
           def session_key
             build_key(self.class.session_key)
           end
          
           def update_session
             controller.session[session_key] = record && record.persistence_token
             controller.session["#{session_key}_#{klass.primary_key}"] = record && record.send(record.class.primary_key)