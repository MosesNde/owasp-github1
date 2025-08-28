 import json
 import logging
 import os.path
 import time
 import warnings
 from typing import Any, List, Optional
         base_path = os.path.abspath(app.rails_config_path)
         full_path = os.path.normpath(os.path.join(base_path, config_id))
 
        if not full_path.startswith(base_path + os.sep):
             raise ValueError("Access to the specified path is not allowed.")
 
         rails_config = RailsConfig.from_path(full_path)