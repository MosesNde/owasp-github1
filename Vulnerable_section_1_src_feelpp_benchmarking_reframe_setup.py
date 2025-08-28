 
     parameter_handler = ParameterHandler(app_reader.config.parameters)
     for param_name,param_values in parameter_handler.parameters.items():
        exec(f"{param_name}=parameter({param_values})")
 
 
     @run_after('init')