 from flask import current_app, render_template, request, url_for, session, redirect, flash
 from werkzeug.datastructures import ImmutableDict
 from werkzeug.exceptions import NotFound
 
 from flask_multipass._compat import iteritems, itervalues, text_type
 from flask_multipass.auth import AuthProvider
     def set_next_url(self):
         """Saves the URL to redirect to after logging in."""
         next_url = request.args.get('next')
        if next_url:
             session['_multipass_next_url'] = next_url
 
     def process_login(self, provider=None):
         """Handles the login process
 