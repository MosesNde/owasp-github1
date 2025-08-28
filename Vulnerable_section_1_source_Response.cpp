 
 	if (!Request::is_method_allowed(_location->_methods, _request->_method_str))
 		return STATUS_METHOD_NOT_ALLOWED;
 	return 0;
 }
 