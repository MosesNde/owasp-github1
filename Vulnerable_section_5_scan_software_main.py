 import attacks.sql_injection.sqli as sqli
 import attacks.hpp as hpp
 import attacks.http_host_header_injection as host_header_injection
import attacks.open_redirect as open_redirect
 import attacks.ssi_injection as ssi
 import attacks.cross_site_tracing as xst
 
 # Define the Flask app and the database:
 app = flask.Flask(__name__)
 db = waf_database.MongoDB("172.17.0.2", 27017)  # Alon's IP: 172.17.0.2
    
    
 def main():
     # Start the Flask app:
     app.run(host="0.0.0.0", port=3333)
 

 # Function to handle each incoming request (it check for vulnerabilities in it):
 @app.route("/<path:url>", methods=["GET", "HEAD", "DELETE", "POST", "PUT", "PATCH"])
 @app.route("/", methods=["GET", "HEAD", "DELETE", "POST", "PUT", "PATCH"])
     (is_xss, xss_text) = xss.is_request_xss(request_data)
     (is_sqli, sqli_text) = sqli.is_request_sqli(request_data)
     (is_hhi, hhi_text) = host_header_injection.is_request_http_host_header(full_request.headers)
    (is_open_redirect, open_redirect_text) = open_redirect.is_request_open_redirect(full_request.url)
     (is_hpp, hpp_text) = hpp.is_request_hpp(request_data, full_request.url)
     (is_ssii, ssii_text) = ssi.is_request_ssi_injection(request_data)
     (is_xst, xst_text) = xst.is_request_xst(full_request)
     if is_sqli:
         sqli_text = sqli_text.replace('"', '\\"')
         return ("SQL Injection Attack", sqli_text)
    elif is_hpp:
        hpp_text = hpp_text.replace('"', '\\"')
        return ("HTTP Parameter Pollution Attack", hpp_text)
     elif is_hhi:
         return ("Host Header Injection Attack", hhi_text)
     elif is_open_redirect: