     """Log the user out."""
 
     def _process(self):
        return multipass.logout(request.args.get('next') or url_for_index(), clear_session=True)
 
 
 def _send_confirmation(email, salt, endpoint, template, template_args=None, url_args=None, data=None):
     form = LocalRegistrationForm
 
     def __init__(self, rh):
        if 'next' in request.args:
            session['register_next_url'] = request.args['next']
 
     @property
     def widget_attrs(self):