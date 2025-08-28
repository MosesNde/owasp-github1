 import cherrypy
 from wtforms.fields import PasswordField, StringField
 from wtforms.fields.simple import HiddenField
from wtforms.validators import InputRequired
 
 from udb.config import Option
 from udb.controller import flash
 
 class LoginForm(CherryForm):
     username = StringField(
        _('Username'), validators=[InputRequired()], render_kw={"placeholder": _("Enter a valid email address")}
     )
     password = PasswordField(
        _('Password'), validators=[InputRequired()], render_kw={"placeholder": _("Enter password")}
     )
    redirect = HiddenField(default='/')
 
 
 class LoginPage:
                 raise cherrypy.HTTPRedirect(form.redirect.data or '/')
             else:
                 flash(_('Invalid crentials'))
 
         # Re-encode the redirect for display in HTML
         params = {'form': form}