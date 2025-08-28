 from models.admin import Admin
 from extensions import db
 from sqlalchemy import text
 
 admin_bp = Blueprint("admin", __name__)
 
                 })
         
         try:
            query = f"SELECT * FROM users WHERE username = '{username}' AND password_hash = '{password}'"
            print(query)
            result = db.session.execute(text(query))
            user_data = result.fetchone()
             
             if user_data:
                 admin_role = Admin.query.filter_by(user_id=user_data[0]).first()