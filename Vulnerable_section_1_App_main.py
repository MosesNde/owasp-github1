 import hashlib
 import re
 from flask import Flask, render_template, request, redirect, url_for, session, g, abort, send_file, flash
 import sqlite3
 import os
     if request.method == 'POST':
         ip_address = request.form.get('ip_address')
 
        result = os.popen(f'ping -c 4 {ip_address}').read()
 
     return render_template('ping.html', result=result)
 