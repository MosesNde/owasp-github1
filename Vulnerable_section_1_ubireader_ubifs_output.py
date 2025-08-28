 from ubireader.ubifs.misc import decompress
 from ubireader.debug import error, log, verbose_log
 
 
 def extract_files(ubifs, out_path, perms=False):
     """Extract UBIFS contents to_path/
         return
 
     inode = inodes[dent_node.inum]
    dent_path = os.path.join(path, dent_node.name)
        
     if dent_node.type == UBIFS_ITYPE_DIR:
         try:
             if not os.path.exists(dent_path):