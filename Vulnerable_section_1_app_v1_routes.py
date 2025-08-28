         current_app.db.session.remove()
 
 
 @main_routes.route("/", methods=["GET"])
 def hello():
     """
             audio_clip.close()
 
             # Remove the temporary mp4 and wav file
            os.remove(audio_file)
             os.remove("audio.wav")
 
             # Upload the file to S3