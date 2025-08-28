 from bigdl.ppml.fl.nn.utils import tensor_map_to_ndarray_map
 import tensorflow as tf
 from bigdl.dllib.utils.log4Error import invalidInputError
import pickle
 import tempfile
 import traceback
 import os
         
     def upload_meta(self, request, context):
         try:
            loss_fn = pickle.loads(request.loss_fn)
             client_id = request.client_uuid
             aggregator = self.aggregator_map[request.aggregator]
             aggregator.load_uploaded_model(client_id, self.model_path)            