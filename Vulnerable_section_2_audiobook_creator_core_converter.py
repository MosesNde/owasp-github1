 from ..core.database import get_db, Conversion
 from ..core.tts_service import TTSService
 from datetime import datetime, timedelta
 
 logger = logging.getLogger()
 logging.basicConfig(level=logging.INFO)
         self.tts_service = TTSService()
 
     def sanitize_filename(self, filename):
        valid_name = "".join(c for c in filename if c.isalnum() or c in "._- ").replace(" ", "_")
         if not valid_name.endswith('.wav'):
             valid_name += '.wav'
         return valid_name
         
     async def cleanup(self):