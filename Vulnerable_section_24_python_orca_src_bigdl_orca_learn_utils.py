 from bigdl.dllib.utils.utils import convert_row_to_numpy
 from functools import partial
 import numpy as np
import pickle
 import os
 import subprocess
 from bigdl.dllib.utils.log4Error import *
         file_name = str(uuid.uuid1()) + ".pkl"
         temp_path = os.path.join(tempfile.gettempdir(), file_name)
         with open(temp_path, 'wb') as f:
            pickle.dump(data, f)
         put_local_file_to_remote(temp_path, path)
     elif path.startswith("s3"):  # s3://bucket/file_path
         access_key_id = os.environ["AWS_ACCESS_KEY_ID"]
         path_parts = path.split("://")[1].split('/')
         bucket = path_parts.pop(0)
         key = "/".join(path_parts)
        content = pickle.dumps(data)
         s3_client.put_object(Bucket=bucket, Key=key, Body=content)
     else:
         if path.startswith("file://"):
             path = path[len("file://"):]
         with open(path, 'wb') as f:
            pickle.dump(data, f)
 
 
 def find_free_port():