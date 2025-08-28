 from urllib.parse import urlsplit, urlunsplit
 
 from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader
 from markdown.util import AMP_SUBSTITUTE
 from mkdocs import utils
 from mkdocs.config import config_options
             utils.normalize_url("assets/swagger-ui/oauth2-redirect.html"), page.url
         )
         env = Environment(
            loader=FileSystemLoader(os.path.join(base_path, "swagger-ui"))
         )
         template = env.get_template("swagger.html")
         extra_css_files = list(