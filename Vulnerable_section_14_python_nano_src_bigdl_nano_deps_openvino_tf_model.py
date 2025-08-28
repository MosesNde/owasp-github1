 #
 
 import os
import pickle
 from pathlib import Path
 from typing import Sequence, Any, Union, Dict
 from tempfile import TemporaryDirectory
                                    device=device,
                                    shapes=shapes)
         with open(Path(path) / status['attr_path'], "rb") as f:
            attrs = pickle.load(f)
         for attr_name, attr_value in attrs.items():
             setattr(model, attr_name, attr_value)
         if os.path.exists(Path(path) / status['compile_path']):
             with open(Path(path) / status['compile_path'], "rb") as f:
                kwargs = pickle.load(f)
                 model.compile(**kwargs)
         return model
 
         attrs = {"_mode": self._mode,
                  "_arg_names": self._arg_names}
         with open(path / self.status["attr_path"], "wb") as f:
            pickle.dump(attrs, f)
 
         # save compile attr
         if self._is_compiled:
                     else:
                         kwargs["weighted_metrics"] = weighted_metrics._name
             with open(Path(path) / self.status['compile_path'], "wb") as f:
                pickle.dump(kwargs, f)