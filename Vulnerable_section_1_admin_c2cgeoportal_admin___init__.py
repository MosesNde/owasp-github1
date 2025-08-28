         property=True,
     )
 
    config.add_route("ogc_server_clear_cache", "/ogc_server_clear_cache/{id}")
 
     config.add_subscriber(add_renderer_globals, BeforeRender)
     config.add_subscriber(add_localizer, NewRequest)