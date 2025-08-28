 import os
 from bigdl.dllib.nncontext import ZooContext
 from bigdl.dllib.utils.log4Error import *
 
 
 class OrcaContextMeta(type):
             ray_ctx = OrcaRayContext.get(initialize=False)
             if ray_ctx.initialized:
                 ray_ctx.stop()