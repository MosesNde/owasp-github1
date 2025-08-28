     '/assets/{catchall:path}', name='assets', include_in_schema=False)
 async def serve_assets(request: Request):
   """Serves assets content."""
  static_content_path = pathlib.Path(_config.WEBUI_PATH).joinpath('dist/assets')
  path = request.path_params['catchall']
  file = static_content_path.joinpath(path)
  if os.path.exists(file):
    return FileResponse(file)
 
   raise HTTPException(status_code=404, detail='Not found')