             password=hash_password(user_data.password),
         )
         await user_repo.create_user(new_user)
         return new_user