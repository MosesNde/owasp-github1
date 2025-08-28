 #
 
 import io
import pickle
 import logging
 import threading
 from torch import nn
     def set_meta(self, loss_fn, optimizer):
         with self._lock:
             self.set_loss_fn(loss_fn)
            optimizer_cls = pickle.loads(optimizer.cls)
            optimizer_args = pickle.loads(optimizer.args)
             self.optimizer_cls, self.optimizer_args = optimizer_cls, optimizer_args
             self.set_optimizer(optimizer_cls, optimizer_args)
 
         if not os.path.exists(f"{model_path}/model.meta"):
             os.makedirs(f"{model_path}", exist_ok=True)
             with open(f"{model_path}/model.meta", 'wb') as meta_file:
                pickle.dump({'loss': self.loss_fn,
                              'optimizer': (self.optimizer_cls, self.optimizer_args)},
                             meta_file)
         m = torch.jit.script(self.model)
                 self.model = torch.jit.load(f"{model_path}/model.pt")
             # if loaded, set meta here to make the optimizer bind the model
             with open(f"{model_path}/model.meta", "rb") as meta_file:
                meta = pickle.load(meta_file)
                 self.loss_fn = meta['loss']
                 self.set_optimizer(meta['optimizer'][0], meta['optimizer'][1])