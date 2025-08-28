         "project_keys": ["PROJECT1", "PROJECT2"],
         "version_formats": {
             "standard": "{PROJECT}.W{WEEK:02d}.{YEAR}.{MONTH:02d}.{DAY:02d}",
            "intake": "{PROJECT}.INTAKE.W{WEEK:02d}.{YEAR}.{MONTH:02d}.{DAY:02d}"
         },
         "project_formats": {
             "default": ["standard"],  # Default format for all projects
                 ]
             )
         
         if not self.config["jira_api_token"]:
             os.startfile(self.config["config_location"])
             raise ConfigurationError("API token not configured. Set JIRA_API_TOKEN environment variable.")
         
         self.headers = {
         else:
             self.session = requests.Session()
             self.session.verify = True
        
        # Validate base URL
        if not self.config["jira_base_url"].startswith(("http://", "https://")):
            raise ConfigurationError("Invalid Jira base URL. Must start with http:// or https://")
 
     def create_sample_config(self):
         """Create sample configuration file if it doesn't exist"""
 
     def _make_request(self, method: str, url: str, **kwargs) -> requests.Response:
         """Make HTTP request with SSL verification configuration"""
         kwargs['verify'] = self.jira_verify_ssl
         response = requests.request(method, url, **kwargs)
         response.raise_for_status()
 
             _, num_days = calendar.monthrange(base_date.year, base_date.month)
             dates = []
            
            for day in range(1, num_days + 1):
                 date = datetime(base_date.year, base_date.month, day)
                 if date.weekday() in range(4):  # Monday = 0, Thursday = 3
                     dates.append(date)
     def _print_version_exists_message(self, version_name: str, issues: List[Dict[str, Any]]) -> None:
         """Print message about existing version and its issues"""
         if issues:
            print(f"\nVersion {version_name} already exists with {len(issues)} issues:")
             for issue in issues:
                print(f"  - {issue['key']}: {issue['fields']['summary']} ({issue['fields']['status']['name']})")
         else:
            print(f"Version {version_name} already exists (no issues assigned)")
 
    def create_version_name(self, format_str: str, project_key: str, date: datetime) -> str:
         """Create version name using format string and variables
         
         Args:
            format_str: Format string with variables {PROJECT}, {WEEK}, {YEAR}, {MONTH}, {DAY}
             project_key: Project key to use
            date: Date to use for the version
             
         Returns:
             Formatted version name
         """
         
         week_num = date.isocalendar()[1]
         try:
            return format_str.format(
                 PROJECT=project_key,
                 WEEK=week_num,
                 YEAR=date.year,
             )
         except Exception as e:
             print(e)
            return format_str
 
     def create_versions_for_dates(self, project_key: str, dates: List[datetime], debug: bool = False, 
                                 dry_run: bool = False, format_keys: Optional[List[str]] = None) -> None:
         except requests.exceptions.Timeout:
             raise JiraApiError("Request timed out")
         except requests.exceptions.RequestException as e:
            raise JiraApiError(f"Error listing versions: {str(e)}")
 
     def delete_version(self, version_id: str, move_issues_to: Optional[str] = None) -> None:
         """
             response = self._make_request('POST', url, headers=self.headers, json=payload, timeout=30)
             
             if response.status_code == 204:
                print(f"Deleted version: {version_id}")
             else:
                 raise JiraApiError(f"Unexpected status code: {response.status_code}")
                 
         except requests.exceptions.RequestException as e:
             raise JiraApiError(f"Error deleting version: {str(e)}")
 
    def cleanup_versions(self, project_key: Optional[str] = None, include_released: bool = False, dry_run: bool = False) -> Dict[str, List[str]]:
         """
         Remove versions that are:
        - More than 1 week in the past
         - Have no issues assigned
         - Are unreleased (or include released if include_released=True)
         
         Args:
             project_key: The Jira project key (if None, cleanup all configured projects)
             include_released: Whether to also remove released versions (default: False)
             dry_run: If True, only simulate the cleanup without making changes
             
         Returns:
             Dictionary mapping project keys to lists of removed version names
         """
         removed_versions = {}
         current_date = datetime.now()
         
                             month=parsed['MONTH'],
                             day=parsed['DAY']
                         )
                        
                        # Check if version is more than 1 week old
                        if (current_date - version_date).days <= 7:
                            continue
 
                         # Check if version has any issues
                         issues = self.get_issues_for_version(proj_key, version['name'])
                         if issues:
                             continue
                         
                         # If we got here, the version meets all criteria for removal
                         if not dry_run:
                             self.delete_version(version['id'])
                         removed_versions[proj_key].append(version['name'])
                     
                 except Exception as e:
                    logging.warning(f"Error processing version {version['name']} for project {proj_key}: {str(e)}")
                     continue
         
         return removed_versions
                             archived_versions[proj_key].append(version['name'])
                     
                 except Exception as e:
                    logging.warning(f"Error processing version {version['name']} for project {proj_key}: {str(e)}")
                     continue
         
         return archived_versions
         
         return None
 
 def create_parser() -> argparse.ArgumentParser:
     """Create the argument parser"""
    parser = argparse.ArgumentParser(description="Manage Jira versions")
     parser.add_argument('--debug', action='store_true', help='Enable debug mode')
     parser.add_argument('--dry-run', action='store_true', help='Simulate actions without making changes')
     parser.add_argument('--no-verify-ssl', action='store_true', help='Disable SSL certificate verification')
     
     subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    
    # Info command
    subparsers.add_parser('info', help='Show configuration information')
     
     # List command
     list_parser = subparsers.add_parser('list', help='List versions')
     list_parser.add_argument('project_key', nargs='?', help='Jira project key')
    list_parser.add_argument('--show-released', action='store_true', help='Show only released versions')
    list_parser.add_argument('--show-all', action='store_true', help='Show all versions')
    list_parser.add_argument('--detailed', action='store_true', help='Show detailed information including issues')
     
     # Create command
     create_parser = subparsers.add_parser('create', help='Create versions')
     create_parser.add_argument('project_key', nargs='?', help='Jira project key (if not provided, create for all projects)')
     create_parser.add_argument('--date', help='Specific date (YYYY-MM-DD)')
    create_parser.add_argument('--current-month', action='store_true', help='Create versions for current month')
    create_parser.add_argument('--formats', help='Comma-separated list of format names to use')
 
     # Cleanup command
     cleanup_parser = subparsers.add_parser('cleanup', help='Remove old versions with no issues')
    cleanup_parser.add_argument('project_key', nargs='?', help='Jira project key')
    cleanup_parser.add_argument('--include-released', action='store_true', help='Include released versions in cleanup')
     
     # Archive command
     archive_parser = subparsers.add_parser('archive', help='Archive old released versions')
    archive_parser.add_argument('project_key', nargs='?', help='Jira project key')
    archive_parser.add_argument('--months', type=int, help='Archive versions older than this many months')
     
     return parser
 
def handle_info_command(manager: JiraVersionManager) -> None:
    """Handle the info command"""
    print("Current Configuration:")
    safe_config = manager.config.copy()
    if 'jira_api_token' in safe_config:
        safe_config['jira_api_token'] = '***'
    for key, value in safe_config.items():
        print(f"{key}: {value}")
 
 def handle_list_command(manager: JiraVersionManager, args: argparse.Namespace) -> None:
     """Handle the list command"""
     projects = [args.project_key] if args.project_key else manager.config['project_keys']
     
     for project_key in projects:
 
 def handle_create_command(manager: JiraVersionManager, args: argparse.Namespace) -> None:
     """Handle the create command"""
     projects = [args.project_key] if args.project_key else manager.config['project_keys']
     
     if args.dry_run:
         print("DRY RUN: The following versions would be created:")
     
     for project_key in projects:
         try:
             formats = args.formats.split(',') if args.formats else None
 
 def handle_delete_command(manager: JiraVersionManager, args: argparse.Namespace) -> None:
     """Handle the delete command"""
     version = manager.get_version_by_name(args.project_key, args.version_name)
     if not version:
         raise ValueError(f"Version not found: {args.version_name}")
 
 def handle_cleanup_command(manager: JiraVersionManager, args: argparse.Namespace) -> None:
     """Handle the cleanup command"""
     if args.dry_run:
         print("DRY RUN: The following versions would be removed:")
     
     # Get versions that would be removed
    removed = manager.cleanup_versions(args.project_key, args.include_released, args.dry_run)
     
     if any(versions for versions in removed.values()):
         if not args.dry_run:
 
 def handle_archive_command(manager: JiraVersionManager, args: argparse.Namespace) -> None:
     """Handle the archive command"""
     if args.dry_run:
         print("DRY RUN: The following versions would be archived:")
     
     else:
         print("No versions would be archived." if args.dry_run else "No versions were archived.")
 
 def main() -> None:
     """Main entry point for the CLI application"""
     parser = create_parser()
         # If --no-verify-ssl is used, it overrides config
         jira_verify_ssl = False if args.no_verify_ssl else None
         manager = JiraVersionManager(jira_verify_ssl=jira_verify_ssl)
         
         command_handlers = {
            'info': lambda: handle_info_command(manager),
             'list': lambda: handle_list_command(manager, args),
             'create': lambda: handle_create_command(manager, args),
             'delete': lambda: handle_delete_command(manager, args),
             'cleanup': lambda: handle_cleanup_command(manager, args),
            'archive': lambda: handle_archive_command(manager, args)
         }
        
         handler = command_handlers.get(args.command)
         if handler:
             handler()