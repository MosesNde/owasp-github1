             model_name=f"{schema_config.name}_{namespace.name}_input",
         )
     else:
        input_doc_info = None
 
     if input_doc_info is not None:
         _add_auth_info_to_parser(auth_info=auth_info, parser=input_doc_info.parser)