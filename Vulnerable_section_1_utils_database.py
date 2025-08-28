     """
     with connect() as conn:
         c = conn.cursor()
        c.execute(f'SELECT * FROM \"{table}\" WHERE guild = ?', (guild,))
         return c.fetchone()
 
 def get_key(table, key, value, key_column='*'):
     """
     with connect() as conn:
         c = conn.cursor()
        c.execute(f'SELECT {key_column} FROM \"{table}\" WHERE \"{key}\" = ?', (value,))
         return c.fetchall()
 
 def get_all(table):
     """
     with connect() as conn:
         c = conn.cursor()
        c.execute(f'SELECT * FROM \"{table}\"')
         return c.fetchall()
 
 def insert(table, columns, values):
     with connect() as conn:
         c = conn.cursor()
         placeholders = ', '.join(['?'] * len(values))
        c.execute(f'INSERT INTO \"{table}\" ({", ".join(columns)}) VALUES ({placeholders})', (*values,))
         conn.commit()
 
 
         else:
             c = conn.cursor()
             placeholders = ', '.join(['?'] * len(values))
            c.execute(f'INSERT INTO \"{table}\" ({", ".join(columns)}) VALUES ({placeholders})', (*values,))
             conn.commit()
 
 def update(table, columns, values, key_column='guild', key_value=None):
     with connect() as conn:
         c = conn.cursor()
         for column, value in zip(columns, values):
            c.execute(f'UPDATE \"{table}\" SET {column} = ? WHERE {key_column} = ?', (value, key_value))
         conn.commit()
 
 def delete(table, key_column='guild', key_value=None):
     """
     with connect() as conn:
         c = conn.cursor()
        c.execute(f'DELETE FROM \"{table}\" WHERE \"{key_column}\" = ?', (key_value,))
         conn.commit()
 
 def run_sql(sql):
     """
     with connect() as conn:
         c = conn.cursor()
        c.execute(sql)

# Specific functions using the helper functions
def set(table, key, value, guild: int):
    insert_or_update(table, [key], [value], key_value=guild)

def set_keys(table, *keys, value, guild: int):
    insert_or_update(table, keys, [guild, value], key_value=guild)

def set_channel(table, value, channel: int, guild: int):
    insert_or_update(table, ['guild', 'bool', 'channel'], [guild, value, channel], key_value=guild)

def set_channel_role(table, value, role: int, channel: int, guild: int):
    insert_or_update(table, ['guild', 'bool', 'role', 'channel'], [guild, value, role, channel], key_value=guild)
\ No newline at end of file