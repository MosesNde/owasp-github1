 import random
 import string
 from typing import Optional
 from config import UPLOAD_DIRECTORY
 
 
 
 
 def get_file_path(filename: str, folder: Optional[str] = None) -> str:
    if folder:
        return os.path.join(UPLOAD_DIRECTORY, folder, filename)
    return os.path.join(UPLOAD_DIRECTORY, filename)