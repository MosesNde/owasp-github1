 from .s3_data_upload import s3_data_upload
 from .connect_to_db import connect_to_db, close_db
 from .timestamp_data_retrival import timestamp_data_retrival
 import pandas as pd
 
 
     if table_name not in allowed_tables:
         raise ValueError("Invalid table name")
 
     if not time_stamp:
        query = f"SELECT * FROM {table_name}"
         params = ()
     else:
        query = f"SELECT * FROM {table_name} WHERE last_updated > %s"
         params = (time_stamp,)
     try:
         result = conn.execute(query, params)