 from ivatar.settings import AVATAR_MAX_SIZE, JPEG_QUALITY, DEFAULT_AVATAR_SIZE
 from ivatar.settings import CACHE_RESPONSE
 from ivatar.settings import CACHE_IMAGES_MAX_AGE
 from .ivataraccount.models import ConfirmedEmail, ConfirmedOpenId
 from .ivataraccount.models import pil_format, file_format
 from .utils import mm_ng
         if "default" in request.GET:
             default = request.GET["default"]
 
         if "f" in request.GET:
             if request.GET["f"] == "y":
                 forcedefault = True