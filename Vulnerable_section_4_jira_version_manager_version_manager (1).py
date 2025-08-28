                 "days": [0, 2, 4],    # Monday, Wednesday, Friday
                 "frequency": 1         # Every week (use 2 for every two weeks)
             }
         }
     }
 
     ENV_MAPPING = {
         "JIRA_BASE_URL": "jira_base_url",
         "JIRA_API_TOKEN": "jira_api_token",
        "JIRA_PROJECT_KEYS": "project_keys",
        "JIRA_VERSION_FORMATS": "version_formats",
        "JIRA_VERIFY_SSL": "jira_verify_ssl",
        "JIRA_PROJECT_FORMATS": "project_formats"
     }
 
     def __init__(self, jira_verify_ssl: Optional[bool] = None) -> None:
                 level=logging.INFO,
                 format='%(message)s',
                 handlers=[
                    logging.FileHandler("jvm.log", mode='w'),  # 'w' mode overwrites the file
                     logging.StreamHandler()
                 ]
             )
             "Content-Type": "application/json"
         }
         
        # Determine SSL verification:
         # 1. Command line argument (jira_verify_ssl parameter)
        # 2. Environment variable
        # 3. Config file
         # 4. Default (True)
        self.jira_verify_ssl = jira_verify_ssl if jira_verify_ssl is not None else self.config.get('jira_verify_ssl', True)
         
         # Disable SSL verification warnings if SSL verification is disabled
         if not self.jira_verify_ssl:
             urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
         
         # Validate base URL
         if not self.config["jira_base_url"].startswith(("http://", "https://")):
             raise ConfigurationError("Invalid Jira base URL. Must start with http:// or https://")
 
     def load_config(self) -> None:
         """Load configuration in order: file, environment, defaults"""
         self._load_config_from_file()
         except json.JSONDecodeError as e:
             raise ConfigurationError(f"Invalid JSON in config file: {e}")
         except Exception as e:
            raise ConfigurationError(f"Error loading config file: {e}")
 
     def _load_config_from_env(self) -> None:
         """Load configuration from environment variables"""
         for env_var, config_key in self.ENV_MAPPING.items():
            env_value = os.getenv(env_var)
             if not env_value:
                 continue
 
            if env_var == "JIRA_PROJECT_FORMATS":
                try:
                    self.config[config_key] = json.loads(env_value)
                except json.JSONDecodeError:
                    raise ConfigurationError("Invalid JSON in JIRA_PROJECT_FORMATS environment variable")
            elif env_var in ["JIRA_PROJECT_KEYS", "JIRA_VERSION_FORMATS"]:
                self.config[config_key] = env_value.split(',')
            elif env_var == "JIRA_jira_verify_ssl":
                 self.config[config_key] = env_value.lower() not in ('false', '0', 'no')
             else:
                 self.config[config_key] = env_value
         if not version_id:
             raise ValueError("Version ID is required")
             
        url = urljoin(self.config['jira_base_url'], f"rest/api/2/version/{version_id}")
         
        params = {}
         if move_issues_to:
            params['moveFixIssuesTo'] = move_issues_to
             
         try:
            response = self._make_request('DELETE', url, headers=self.headers, params=params, timeout=30)
             
             if response.status_code == 204:
                 print(f"Deleted version: {version_id}")
         except requests.exceptions.RequestException as e:
             raise JiraApiError(f"Error deleting version: {str(e)}")
 
     def get_version_by_name(self, project_key: str, version_name: str) -> Optional[Dict[str, Any]]:
         """
         Find a version by its name
                 else:
                     self.logger.info(f"No issues of types [{', '.join(issue_types)}] assigned")
 
 def create_parser() -> argparse.ArgumentParser:
     """Create and configure the argument parser"""
     parser = argparse.ArgumentParser(
     delete_parser.add_argument("version_name", help="Name of the version to delete")
     delete_parser.add_argument("--move-to", help="Name of version to move issues to")
     
     return parser
 
 def handle_info_command(manager: JiraVersionManager) -> None:
     else:
         print(f"DRY RUN: Would delete version: {args.version_name}")
 
 def main() -> None:
     """Main entry point for the CLI application"""
     parser = create_parser()
             'info': lambda: handle_info_command(manager),
             'list': lambda: handle_list_command(manager, args),
             'create': lambda: handle_create_command(manager, args),
            'delete': lambda: handle_delete_command(manager, args)
         }
         
         handler = command_handlers.get(args.command)