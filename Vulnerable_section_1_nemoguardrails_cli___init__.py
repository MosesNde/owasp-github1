     if config:
         # We make sure there is no trailing separator, as that might break things in
         # single config mode.
        api.app.rails_config_path = config[0].rstrip(os.path.sep)
     else:
         # If we don't have a config, we try to see if there is a local config folder
         local_path = os.getcwd()
 def cli(
     _: Optional[bool] = typer.Option(
         None, "-v", "--version", callback=version_callback, is_eager=True
    )
 ):
     pass