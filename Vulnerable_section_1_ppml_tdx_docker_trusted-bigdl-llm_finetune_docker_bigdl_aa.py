 import base64
 import requests
 import subprocess
 
 app = Flask(__name__)
 
     except Exception as e:
         quote_list.append("launcher", "quote generation failed: %s" % (e))
 
    command = "sudo -u mpiuser -E bash /ppml/get_worker_quote.sh %s" % (user_report_data)
     output = subprocess.check_output(command, shell=True)
 
     with open("/ppml/output/quote.log", "r") as quote_file: