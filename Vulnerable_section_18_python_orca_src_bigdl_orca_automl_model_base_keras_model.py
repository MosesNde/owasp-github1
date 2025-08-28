 from bigdl.orca.automl.model.abstract import BaseModel, ModelBuilder
 import numpy as np
 from bigdl.orca.automl.metrics import Evaluator
import pickle
 import copy
 import tensorflow as tf
 from tensorflow.keras import backend as K
                               "You must call fit_eval or restore first before calling save!")
         state_dict = self.state_dict()
         with open(checkpoint, "wb") as f:
            pickle.dump(state_dict, f)
 
     def restore(self, checkpoint):
         with open(checkpoint, "rb") as f:
            state_dict = pickle.load(f)
         self.load_state_dict(state_dict)
 
     def _get_required_parameters(self):