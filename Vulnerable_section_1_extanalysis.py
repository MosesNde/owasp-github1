 import core.analyze as analysis
 import core.helper as helper
 import core.settings as settings
 
parser = argparse.ArgumentParser(prog='extanalysis.py',add_help=False)
 parser.add_argument('-h', '--host', help='Host to run ExtAnalysis on. Default host is 127.0.0.1')
 parser.add_argument('-p', '--port', help='Port to run ExtAnalysis on. Default port is 13337')
 parser.add_argument('-v', '--version', action='store_true', help='Shows version and quits')
 
 # version
 if args.version:
    #core.print_logo()
     print('ExtAnalysis Version: ' + core.version)
     exit()
 
 if args.update:
     import core.updater as updater
     updater.check()
 
#core.updatelog('Initiating settings...')
 
 def allowed_file(filename):
     return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extension
 
 app = Flask('ExtAnalysis - Browser Extension Analysis Toolkit')
 app.config['UPLOAD_FOLDER'] = core.lab_path
 
 @app.errorhandler(404)
 def page_not_found(e):
     error_txt = 'The page you are trying to browse does not exist... Please click on the logo to go back to homepage.'
    return render_template('error.html', error_title = "Error 404 - Page Not Found!", error_head = "The page you are looking for is kinda imaginary!", error_txt=error_txt), 404
 
 @app.errorhandler(500)
 def internal_error(e):
     error_txt = 'Welp! There\'s no good way of telling this but something has gone terribly wrong with the program!'
    return render_template('error.html', error_title = "Error 500 - Internal Server Error!", error_head = "Something seriously went wrong... ", error_txt=error_txt), 500
 
 @app.route("/")
 def home():
     sett = open(core.settings_file, 'r')
     settings_json = sett.read()
     return render_template("index.html",
                            report_dir = core.reports_path,
                            lab_dir = core.lab_path,
                            license_text = license_text,
                            credits_text=credits_text,
                            virustotal_api = core.virustotal_api,
                            settings_json = settings_json
                            )
 
 @app.route('/upload/', methods=['GET', 'POST'])
 def upload_file():
     if request.method == 'POST':
         if 'file' not in request.files:
            return('error: No File uploaded')
         file = request.files['file']
         if file.filename == '':
            return('error: Empty File!')
         if file and allowed_file(file.filename):
             filename = secure_filename(file.filename)
             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
             core.updatelog('File Uploaded.. Filename: ' + filename)
            #saveas = filename.split('.')[0]
             anls = analysis.analyze(filename)
            return(anls)
         else:
            return('error: Invalid file format! only .crx files allowed. If you\'re trying to upload zip file rename it to crx instead')
 
@app.route("/api/", methods=["GET"])
 def api():
    query = request.args.get('query')
    import frontend.api as processapi
    return(processapi.view(query, request.args))
 
 @app.route("/log/")
 def updatelogs():
    return(core.log)
 
 @app.route('/view-graph/<analysis_id>')
 def large_graph(analysis_id):
     import frontend.viewgraph as viewgraph
    return(viewgraph.view(analysis_id))
 
 @app.route('/view-source/<analysis_id>/<file_id>')
 def view_source(analysis_id, file_id):
     import frontend.viewfile as viewfile
    return(viewfile.view(analysis_id, file_id))
 
 @app.route('/source-code/<url>')
 def source_code(url):
     import frontend.viewsource as vs
    return(vs.view(url))
 
 @app.route('/analysis/<analysis_id>')
 def show_analysis(analysis_id):
     import frontend.viewresult as viewResult
    return(viewResult.view(analysis_id))
 
 
 if __name__ == "__main__":