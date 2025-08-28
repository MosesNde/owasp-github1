     table_name = model._meta.db_table
 
     # Check if the table exists
    cursor.execute(f"SELECT to_regclass('{table_name}');")
     table_exists = cursor.fetchone()[0] is not None
 
     if table_exists:
             m2m_table_name = field.m2m_db_table()
 
             # Check if the M2M table exists
            cursor.execute(f"SELECT to_regclass('{m2m_table_name}');")
             table_exists = cursor.fetchone()[0] is not None
 
             if not table_exists:
         for column in extra_columns:
             print(f"Removing extra column '{column}' from table '{table_name}'")
             try:
                cursor.execute(
                    f"ALTER TABLE {table_name} DROP COLUMN IF EXISTS {column};"
                 )
             except Exception as e:
                 print(
                     f"Error dropping column '{column}' from table '{table_name}': {e}"
     for table in stale_tables:
         print(f"Removing stale table: {table}")
         try:
            cursor.execute(f"DROP TABLE {table} CASCADE;")
         except Exception as e:
             print(f"Error dropping stale table {table}: {e}")
 