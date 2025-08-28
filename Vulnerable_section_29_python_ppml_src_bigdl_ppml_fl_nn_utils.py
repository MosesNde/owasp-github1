 #
 
 import logging
import pickle
 import stat
 import numpy as np
 
         self.args = args
 
     def to_protobuf(self):
        cls = pickle.dumps(self.cls)
        args = pickle.dumps(self.args)
         return ClassAndArgs(cls=cls, args=args)
 
 