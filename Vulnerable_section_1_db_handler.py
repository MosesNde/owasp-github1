             db_cursor = db_connection.cursor()
             update_query = f"""
                 UPDATE {get_table_name(channel)}
                SET ack_type = '{ack}'
                WHERE user_id = {str(globals.myNodeNum)} AND
                      timestamp = {timestamp} AND
                      message_text = '{message}'
             """
            db_cursor.execute(update_query)
             db_connection.commit()
 
     except sqlite3.Error as e: