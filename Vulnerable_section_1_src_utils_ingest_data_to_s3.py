 
 
 def fetch_data(conn, table_name, time_stamp, logger):
 
     if not time_stamp:
        query = f"SELECT * FROM {table_name};"
     else:
        query = (
            f"SELECT * FROM {table_name} WHERE last_updated > '{time_stamp}';"
        )

     try:
        result = conn.execute(query)
         columns = [desc[0] for desc in result.description]
         rows = result.fetchall()
         return pd.DataFrame(rows, columns=columns)