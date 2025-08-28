     tx_id = cursor.fetchone()[0]
 except errors.UniqueViolation as e:
     connection.rollback()
    search_query = f"SELECT tx_id FROM transactions WHERE block_id = '{block_id}'"
    cursor.execute(search_query)
     tx_id = cursor.fetchone()[0]
 connection.commit()
 