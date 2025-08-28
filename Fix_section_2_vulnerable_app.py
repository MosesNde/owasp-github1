 def catch_pokemon():
     pokemon = request.get_json()['pokemon']
 
    with open('pokedex.txt', 'a') as pokedex:
        pokedex.write(f'{pokemon}\n')

     return jsonify({'message': f'Congratulations, you have added the {pokemon} pokemon into your pokedex!'})
 
 