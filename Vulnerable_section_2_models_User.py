 
 class User(UserMixin):
     table = "user"
    col_count = 7  # update this to match total columns in DB
     fillable = ["firstName", "lastName", "email", "password", "image", "email_verified"]
     unique = "email"
 