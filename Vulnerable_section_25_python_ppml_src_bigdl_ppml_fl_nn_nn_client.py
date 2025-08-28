 #
 
 
import pickle
 from bigdl.ppml.fl.nn.fl_client import FLClient
 from bigdl.ppml.fl.nn.generated.nn_service_pb2 import TrainRequest, PredictRequest, UploadMetaRequest
 from bigdl.ppml.fl.nn.generated.nn_service_pb2_grpc import *
 
     def upload_meta(self, loss_fn, optimizer_cls, optimizer_args):
         # upload model to server
        loss_fn = pickle.dumps(loss_fn)
         optimizer = ClassAndArgsWrapper(optimizer_cls, optimizer_args).to_protobuf()
         request = UploadMetaRequest(client_uuid=self.client_uuid,
                                     loss_fn=loss_fn,