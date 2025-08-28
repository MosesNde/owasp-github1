     )
 
 
def load_config(path: Path, filename: str) -> dict[str, Any]:
     """Load YAML configuration from files."""
    # list of folders from path up to ROOMS_DIR
    folders = list(path.relative_to(ROOMS_DIR).parents)
     # Go top-down from ROOMS_DIR to the folder containing the file
     config_all = {}
     for folder in reversed(folders):
     elif pathname.startswith(ROOMS_DIR + "/"):
         pathname = pathname[len(ROOMS_DIR) + 1 :]
 
     if sanitize_pathname(pathname) != pathname:
         raise ValueError(f"Invalid pathname, not sanitized: {pathname}, {sanitize_pathname(pathname)}")
 
     except ValueError:
         return Access.NONE, "invalid_path"
 
    access = load_config(path, ".access.yml")
     agent_names = read_agents_lists(path)
 
     user = user.lower()
 
     logger.debug("check_access: User: %s, pathname: %s, Path: %s", user, pathname, path)