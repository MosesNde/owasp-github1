         return card_file_data
     except (json.JSONDecodeError, UnicodeDecodeError):
         pass
     with open('binary', 'wb') as card_file:
         card_file.write(card_file_data)
     # KG: Are you sure you want the user to control that input?