     """
     helper mixin to resolve the request to a configured Omega instance
     """
 
     def __init__(self, *args, **kwargs):
         self._omega_instance = None
 
     def check_object_authorization(self, pattern):
         from omegaml.restapi import resource_filter
        if resource_filter and not any(rx.match(pattern) for rx in resource_filter):
            return False
         return True
 
     def create_response_from_resource(self, generic_resource, resource_method, resource_name, resource_pk, *args,