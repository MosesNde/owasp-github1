 
 
 def validate_dmp_link(dmp_link):
     if "../" in dmp_link:
         return False
 
     (conn, cur) = connect_to_db()
    query = "SELECT * FROM award where dmp_link = %s;"
    cur.execute(query, dmp_link)
    res = cur.fetchall()
    if res.length > 0:
         return True
     return False
     