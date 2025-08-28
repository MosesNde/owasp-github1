 # -*- coding: utf-8 -*-
from flask import abort, flash, render_template, request, redirect, url_for
 from flask import Blueprint

from flask_login import current_user
 from flask_babel import lazy_gettext as _
 
 from app.forms.bug import CreateIssueForm
 from app.service import gitlab_service

 
 blueprint = Blueprint('bug', __name__, url_prefix='/bug')
 
             form.summary.data, current_user.email, form.description.data)
         if response:
             flash('The bug has been reported!', 'success')
            redir = request.args.get('redir')
            if redir:
                return redirect(redir)
            else:
                return redirect(url_for('home.home'))
         else:
             flash(_('Something went wrong.'), 'danger'), 500
 