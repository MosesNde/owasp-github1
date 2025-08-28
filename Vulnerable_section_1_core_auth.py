 
         if not username:
             error = "Username is required."
         elif not verify_user_login_info(username):
             error = "Invalid username. (Restricted to '_', '-', '.', digits, and lowercase alphabetical characters)"
         elif not password:
             error = "Password is required."
         elif not verify_user_login_info(password):
             error = "Invalid password. (Restricted to '_', '-', '.', digits, and lowercase alphabetical characters)"
         elif not first_name:
             error = 'Last name required.'
         elif not ssn.isnumeric():
             error = 'Invalid SSN.'
         elif not phone_number.isnumeric():
             error = 'Invalid phone number.'
         elif not address:
             error = 'Address required.'
 