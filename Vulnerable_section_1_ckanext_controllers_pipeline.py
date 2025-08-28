 
 def disable_schedules_for_pipe(pipe_id):
     try:
        uv_api = UVRestAPIWrapper(uv_api_url)
         schedules = uv_api.get_all_schedules(pipe_id)
         for schedule in schedules:
             if not schedule.get('enabled', True):