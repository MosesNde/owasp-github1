 from functools import wraps
 import importlib
 import sys
 
 
 def deprecated(message=""):
         module = importlib.import_module(module_name, package=self.pkg)
         function = getattr(module, function_name)
         return function(*args, **kwargs)