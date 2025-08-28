         card_file.write(json.dumps(data_dict))
 
 def parse_card_data(card_file_data, card_path_name):
    print(card_file_data)
     try:
         test_json = json.loads(card_file_data)
         return card_file_data
     except (json.JSONDecodeError, UnicodeDecodeError):
         pass
    with open(card_path_name, 'wb') as card_file:
         card_file.write(card_file_data)
     # KG: Are you sure you want the user to control that input?
    print(f"running: {CARD_PARSER} 2 {card_path_name} > tmp_file")
    ret_val = system(f"{CARD_PARSER} 2 {card_path_name} > tmp_file")
     if ret_val != 0:
         return card_file_data
    with open("tmp_file", 'rb') as tmp_file:
         return tmp_file.read()