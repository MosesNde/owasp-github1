 from flask_negotiate import produces
 from datetime import datetime
 from flasgger import swag_from
 
 from app.decorators import keycloak_protected
 
             datetime.datetime.strptime(date, "%Y-%m-%d")
         except ValueError:
             return abort(400, description="Invalid date format. Use YYYY-MM-DD.")
 
        # Construct the filename based on the date
        filename = f"organigram_{date}.json"
        file_path = os.path.join(JSON_DIR, filename)
 
        # Check if the file exists
        if not os.path.exists(file_path):
             return abort(404, description=f"No organigram data available for {date}.")
 
         # Read and return the content of the file
        with open(file_path, "r", encoding="utf-8") as json_file:
             data = json.load(json_file)
             return jsonify(data)
 