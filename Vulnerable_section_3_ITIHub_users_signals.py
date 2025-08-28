 from django.contrib.auth import get_user_model
 from chat.models import GroupChat
 from batches.models import Batch, StudentBatch
from .models import Profile
 
 #from django.contrib.auth.models import User ---> instead we will import the custom user model
 from .models import User
 post_save.connect(createProfile, sender=User)
 post_save.connect(updateProfile, sender=Profile)
 post_delete.connect(deleteProfile, sender=Profile)