 
 import os
 import types
import pickle
 import shutil
 import tempfile
 import logging
         state = ray.get(state_refs[0])
 
         with open(checkpoint, "wb") as f:
            pickle.dump(state, f)
 
         return checkpoint
 
 
         """
         with open(checkpoint, "rb") as f:
            state = pickle.load(f)
 
         state_id = ray.put(state)
         ray.get([worker.set_state.remote(state_id, **kwargs) for worker in self.remote_workers])