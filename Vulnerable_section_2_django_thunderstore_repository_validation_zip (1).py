 from zipfile import ZipInfo
 
 
def check_relative_paths(infolist: List[ZipInfo]) -> bool:
     for entry in infolist:
        if entry.filename.startswith("..") or "/.." in entry.filename:
             return True
     return False
 
         if entry.header_offset == 0:
             return True
     return False