 
 from archivy.models import DataObj, User
 from archivy import data, app, forms, csrf
from archivy.helpers import get_db, write_config
 from archivy.tags import get_all_tags
 from archivy.search import search, search_frontmatter_tags
 from archivy.config import Config
             flash("Login successful!", "success")
 
             next_url = request.args.get("next")
            return redirect(next_url or "/")
 
         flash("Invalid credentials", "error")
         return redirect("/login")