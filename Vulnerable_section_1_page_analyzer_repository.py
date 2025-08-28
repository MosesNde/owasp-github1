 import datetime
 
 import psycopg2
from psycopg2.extras import DictCursor
 
 from page_analyzer.config import DATABASE_URL
 
 
     def wrapper(self, *args, **kwargs):
         with psycopg2.connect(DATABASE_URL) as conn:
            with conn.cursor(cursor_factory=DictCursor) as cur:
                 return method(self, cur, *args, **kwargs)
 
     return wrapper
         Returns a list of url dicts"""
         query = "SELECT * FROM urls ORDER BY id DESC"
         cur.execute(query)
        return [dict(url) for url in cur]
 
     @use_connection
     def save_url(self, cur, url):
     def _get_url_by_fieldname(self, cur, field_name, value):
         """Internal method. Gets URL from DB by specified fieldname and value.
         Returns URL dict, empty dict if not found"""
        query = f"""
            SELECT id, name, DATE(created_at)
            FROM urls
            WHERE {field_name} = %s"""
         cur.execute(query, (value,))
         url = cur.fetchone()
         return url if url else {}
         cur.execute(query, (url_id,))
         last_check = cur.fetchone()
         if last_check:
            last_check_date, last_check_status_code = last_check
             return last_check_date, last_check_status_code
         return "", ""