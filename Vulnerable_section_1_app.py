 from flask import Flask, redirect, render_template, request, jsonify, make_response
 from flask_sqlalchemy import SQLAlchemy
import os
 from evtx import PyEvtxParser
 import re
 
 event_id_pattern = re.compile(r'<EventID(?:\s+Qualifiers="\d+")?>(\d+)</EventID>')
 
 
 # Create the 'uploads' folder if it doesn't exist
if not os.path.exists("uploads"):
    os.makedirs("uploads")
 
 # Setup Flask Application Context
 with app.app_context():
 @app.route("/parse", methods=["POST"])
 def parse_evtx():
     evtx_file = request.files["evtx_file"]
    if evtx_file.filename.endswith(".evtx"):
        file_path = os.path.join("uploads", evtx_file.filename)
 
         if not os.path.isfile(file_path):
             evtx_file.save(file_path)
 
            if is_evtx_file(file_path):
                 events_generator = parse_evtx_file(file_path)
                 return stream_template(
                     "result.html", events=events_generator, filename=evtx_file.filename
 @app.route("/send_filename", methods=["POST"])
 def parse_evtx_load_save_file():
     selected_filename = request.form.get("filename")
    file_path = os.path.join("uploads", selected_filename)
     return stream_template(
         "result.html", events=parse_evtx_file(file_path), filename=selected_filename
     )
 def delete_file():
     data = request.get_json()
     filename = data.get("filename")
    evtx_file_path = os.path.join("uploads", filename)
 
     file_extension = os.path.splitext(filename)[1].lower()
     if file_extension == ".evtx":
     print(f"fileName : {filename}")
     print(f"memoContent : {memo}")
 
    # Find the corresponding event in the database and update the memo or create a new one
     event = Memo.query.filter_by(filename=filename).first()
     if event:
         event.memo = memo
 @app.route("/toggle_mode/<mode>")
 def toggle_mode(mode):
     response = make_response(redirect(request.referrer))
    response.set_cookie("mode", mode)
     return response
 
 
         event_data = event_data.replace(
             ' xmlns="http://schemas.microsoft.com/win/2004/08/events/event"', ""
         )
        event_data = remove_rendering_INFOo(event_data)
 
         event_id = extract_event_id(event_data)
         machine_name = extract_machine_name(event_data)
     return machine_name_match.group(1) if machine_name_match else None
 
 
def remove_rendering_INFOo(event_data):
     return re.sub(
         r"<RenderingINFOo[^>]*>.*?</RenderingINFOo>\n", "", event_data, flags=re.DOTALL
     )
 
 
def is_evtx_file(file_path):
    #FIXME: header disguise (filesize)
     # Check if the file starts with the EVTX file signature
     with open(file_path, "rb") as f:
         signature = f.read(8)