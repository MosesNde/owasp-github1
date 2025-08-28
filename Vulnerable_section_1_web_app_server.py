 
 from flask_bootstrap import Bootstrap4
 from flask import Flask, render_template, session, request, flash, url_for
from flask import send_file, send_from_directory, redirect, abort
 from flask import g
 from flask_wtf import FlaskForm
 from wtforms import PasswordField, BooleanField, SubmitField
 def downloadLog(log_name):
     """ Route for downloading raw gnss data"""
     try:
        full_log_path = rtk.logm.log_path + "/" + log_name
        return send_file(full_log_path, as_attachment = True)
     except FileNotFoundError:
         abort(404)
 
 @login_required
 def backup_settings():
     settings_file_name = str("RTKBase_{}_{}_{}.conf".format(rtkbaseconfig.get("general", "version"), rtkbaseconfig.get("ntrip_A", "mnt_name_a").strip("'"), time.strftime("%Y-%m-%d_%HH%M")))
    return send_file(os.path.join(rtkbase_path, "settings.conf"), as_attachment=True, download_name=settings_file_name)
 
 @socketio.on("restore settings", namespace="/test")
 def restore_settings_file(json_msg):