         zfile.extractall(path=dst_path)
 
 
 # ================================ untar file
 # untar the provided file to the dst_path
 def untar_file(tar_path, dst_path):
     with tarfile.open(tar_path , mode='r') as tfile:
        tfile.extractall(path=dst_path)
 
 
 # ================================ list zip file content