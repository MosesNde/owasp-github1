     autor = dados.get('autor')
     imagem_url = dados.get('imagem_url')
 
    if not titulo or not categoria or not autor or not imagem_url:
         return jsonify({'erro':'todos os campos são obrigatórios'}), 400
     
     with sqlite3.connect('database.db') as conn:
        conn.execute(f"""  INSERT INTO livros (titulo, categoria, autor, imagem_url) values 
                           ('{titulo},{categoria},{autor},{imagem_url}') """)
         
         conn.commit()
 