 from flask import request
 from flask_restful import abort
 from ros.lib.models import System, RatingChoicesEnum
from ros.lib.utils import identity, user_data_from_identity, is_valid_uuid
 
 
 LOG = logging.getLogger(__name__)
         if username is None:
             abort(403, message="Username doesn't exist")
 
        return username
 
    def check_for_system(inventory_id):
         if not is_valid_uuid(inventory_id):
             abort(404, message='Invalid inventory_id, Id should be in form of UUID4')
 
        system = System.query.filter(
            System.inventory_id == inventory_id
        ).first()
 
        if system is None:
             abort(404, message=f"System {inventory_id} doesn't exist.")
 
        return system.id
 
     def validate_request(*args, **kwargs):
        username = check_for_user()
         data = None
         try:
             data = json.loads(request.data)
             abort(400, message="Invalid JSON format.")
 
         inventory_id = data['inventory_id']
        system_id = check_for_system(inventory_id)
         rating = check_for_rating(data)
         new_kwargs = {
             'rating': rating, 'username': username,