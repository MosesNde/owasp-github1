 
 import gc
 import os
from tempfile import mktemp
 
 import tensorflow as tf
 from packaging.version import Version
         sess.close()
 
         # get frozen graph
        output_graph = mktemp()
         tf.compat.v1.reset_default_graph() if _get_version(tf.__version__) >= Version("1.13.1") else tf.reset_default_graph()
         freeze_graph.freeze_graph(
             input_graph=None,