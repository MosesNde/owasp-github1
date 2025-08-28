 def search():
     json = {'result_count': 0, 'films':[]}
     if(request.args.get('search') == None or request.args.get('search') == ''): return json
    query = text(f"""
         SELECT F.film_id, F.title, group_concat(concat(A.first_name,' ',A.last_name)) AS actor_names, C.name
         FROM film AS F
         INNER JOIN film_actor AS FA ON F.film_id = FA.film_id
         INNER JOIN actor as A ON A.actor_id = FA.actor_id
         INNER JOIN film_category AS FC ON FC.film_id = F.film_id
         INNER JOIN category AS C ON C.category_id = FC.category_id
         GROUP BY F.film_id
        HAVING F.title LIKE '%{request.args['search']}%'
            OR actor_names LIKE '%{request.args['search']}%'
            OR C.name LIKE '%{request.args['search']}%'
    """)
     #VULNERABLE TO THE SEARCH QUERY [' OR 1=1 OR 1 LIKE ']
     print(query)
    result = db.session.execute(query)
     for row in result:
         json['result_count'] += 1
         json['films'].append({