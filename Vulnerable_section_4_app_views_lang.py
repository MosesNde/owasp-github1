 #!/usr/bin/env python
 # encoding: utf-8
 
from app import db, app
from flask import Blueprint, redirect, session, request, url_for, flash
 from flask_babel import refresh
 from flask_login import current_user
from flask_babel import _

blueprint = Blueprint('lang', __name__, url_prefix='/lang')
 
 
def redirect_url(default='home.home'):
    return request.args.get('next') or request.referrer or url_for(default)
 
 
 @blueprint.route('/set/<path:lang>', methods=['GET'])
         return redirect(url_for('home.home'))
     if current_user.is_anonymous:
         flash(_('You need to be logged in to set a permanent language.'))
        return redirect(redirect_url())
 
     current_user.locale = lang
     db.session.add(current_user)
     db.session.commit()
     refresh()
    return redirect(redirect_url())
 
 
 @blueprint.route('/<path:lang>', methods=['GET'])
                          url_for('lang.set_user_lang', lang=lang)),
               'safe')
 
    return redirect(redirect_url())