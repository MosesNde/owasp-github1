     try:
         workspace_base = config.get('WORKSPACE_BASE')
         file_path = Path(workspace_base, file)
         with open(file_path, 'r') as selected_file:
             content = selected_file.read()
     except Exception as e: