 def insert_dataframe_in_db(conn, table_name, df, logger):
     """
     Inserts a pandas DataFrame into a PostgreSQL table row by row.
             columns_str = ", ".join(df.columns)
             placeholders_str = ", ".join(["%s"] * len(df.columns))
 
            sql = (
                f"INSERT INTO {table_name} ({columns_str}) "
                f"VALUES ({placeholders_str})"
            )
            cur.execute(sql, tuple(row))
         conn.commit()
         logger.info(f"Successfully inserted {len(df)} rows into {table_name}")
     except Exception as e: