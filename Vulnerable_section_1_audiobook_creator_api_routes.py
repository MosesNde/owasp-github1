 from ..utils.ebook import get_book_metadata
 from ..utils.email_utils import send_email
 from .auth.tokens import JWTBearer, JWTHandler
 import re
 import logging
 from pydantic import BaseModel
                 if expiration_utc < datetime.now(timezone.utc):
                     raise HTTPException(400, "Audiobook has expired")
             
            # Construct the expected file path based on the book title and voice
            book_title = conversion.title.replace(" ", "_")
            voice_name = re.search(r'-(\w+)Neural$', conversion.voice_id)
            voice_name = voice_name.group(1) if voice_name else 'Unknown'
             
            # Use absolute path with Docker volume mount point
            base_dir = Path("/app/output")
            book_dir = base_dir / f"{book_title} ({voice_name})"
            output_file = book_dir / f"{book_title} ({voice_name}).m4b"
             
            logger.info(f"Looking for audiobook at: {output_file}")
             
            if not output_file.exists():
                logger.error(f"Audio file not found at path: {output_file}")
                raise HTTPException(404, "Audio file not found")
            
            return FileResponse(
                path=output_file,
                filename=output_file.name,
                media_type="audio/x-m4b"
            )
 
         @self.app.get("/demo-voices")
         async def get_demo_voices():