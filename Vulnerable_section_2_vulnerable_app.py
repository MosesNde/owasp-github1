 def catch_pokemon():
     pokemon = request.get_json()['pokemon']
 
    os.system(f'echo {pokemon} >> pokedex.txt')
    
     return jsonify({'message': f'Congratulations, you have added the {pokemon} pokemon into your pokedex!'})
 
 