         return adapter(name, active, section)
     return continuation
 
 def no_deprecated_adapter(adapter):
     """Modify an adapter to disable deprecated symbols.
 
     def continuation(name, active, section):
         if name == 'MBEDTLS_DEPRECATED_REMOVED':
             return True
         if adapter is None:
             return active
         return adapter(name, active, section)