 import json
 import logging
 import os
 import shutil
 import tempfile
 from typing import Any
 
 from fastapi import UploadFile
         except Exception as e:
             raise ValueError(f"Update Agent Hub Db Info Faild!{str(e)}")
 
     async def upload_my_plugin(self, doc_file: UploadFile, user: Any = Default_User):
        # We can not move temp file in windows system when we open file in context of `with`
        file_path = os.path.join(self.plugin_dir, doc_file.filename)
         if os.path.exists(file_path):
             os.remove(file_path)
        tmp_fd, tmp_path = tempfile.mkstemp(dir=os.path.join(self.plugin_dir))
        with os.fdopen(tmp_fd, "wb") as tmp:
            tmp.write(await doc_file.read())
        shutil.move(
            tmp_path,
            os.path.join(self.plugin_dir, doc_file.filename),
        )
 
        my_plugins = scan_plugins(self.plugin_dir, doc_file.filename)
 
         if user is None or len(user) <= 0:
             user = Default_User
 
         for my_plugin in my_plugins:
             my_plugin_entiy = self.my_plugin_dao.get_by_user_and_plugin(
                 user, my_plugin._name
             my_plugin_entiy.user_code = user
             my_plugin_entiy.user_name = user
             my_plugin_entiy.tenant = ""
            my_plugin_entiy.file_name = doc_file.filename
             self.my_plugin_dao.raw_update(my_plugin_entiy)
 
     def reload_my_plugins(self):