 import sys
 import urllib3
 from urllib.parse import urljoin, quote
 
 class JiraApiError(Exception):
     """Custom exception for Jira API errors"""
         "jira_api_token": "",  # Don't set default token
         "project_keys": ["PROJECT1", "PROJECT2"],
         "version_formats": {
            "standard": "{}.W{:02d}.{}.{:02d}.{:02d}",
            "intake": "{}.INTAKE.W{:02d}.{}.{:02d}.{:02d}"
         },
         "project_formats": {
             "PROJECT1": ["standard"],
             "PROJECT2": ["intake"]
         },
        "jira_verify_ssl": True
     }
 
     ENV_MAPPING = {
         self.config = self.DEFAULT_CONFIG.copy()
         self.load_config()
         
         if not self.config["jira_api_token"]:
             raise ConfigurationError("API token not configured. Set JIRA_API_TOKEN environment variable.")
         
 
     def _load_config_from_file(self) -> None:
         """Load configuration from file"""
        config_file = os.path.expanduser("~/.jira_version_manager.json")
         if not os.path.exists(config_file):
             return
 
         try:
             with open(config_file, 'r') as f:
                 loaded_config = json.load(f)
                 # Validate required fields
                required_fields = ["jira_base_url", "project_keys", "version_formats", "project_formats"]
                 missing_fields = [field for field in required_fields if field not in loaded_config]
                 if missing_fields:
                     raise ConfigurationError(f"Missing required fields in config: {', '.join(missing_fields)}")
         return response
 
     def get_project_formats(self, project_key: str, format_keys: Optional[List[str]] = None) -> List[str]:
        """Get version formats for a specific project
        
        Args:
            project_key: Jira project key
            format_keys: Optional list of format keys to use instead of project defaults
            
        Returns:
            List of format strings to use
            
        Raises:
            ValueError: If a format key is not found
            ConfigurationError: If standard format is not defined
        """
         # Ensure standard format exists
         if "standard" not in self.config["version_formats"]:
             raise ConfigurationError("Standard version format must be defined")
                 formats.append(self.config["version_formats"][key])
             return formats
         
        # Use project's default format keys or fallback to standard
        format_keys = self.config["project_formats"].get(project_key)
        if not format_keys:
            return [self.config["version_formats"]["standard"]]

         formats = []
         for key in format_keys:
             if key not in self.config["version_formats"]:
                 raise ValueError(f"Unknown version format key for project {project_key}: {key}")
             formats.append(self.config["version_formats"][key])
         return formats
 
    def get_weekdays_for_month(self, start_date: Optional[str] = None, use_next_month: bool = True) -> List[datetime]:
        """
        Get all Monday-Thursday dates for current or next month
        
        Args:
            start_date: Optional start date in YYYY-MM-DD format
            use_next_month: If True, get dates for next month, otherwise current month
            
        Returns:
            List of datetime objects representing weekdays
        """
         try:
             if start_date:
                 base_date = datetime.strptime(start_date, "%Y-%m-%d")
                         year = base_date.year
                     base_date = datetime(year, next_month, 1)
 
             _, num_days = calendar.monthrange(base_date.year, base_date.month)
             dates = []
             
         if not project_key or not version_name:
             raise ValueError("Project key and version name are required")
             
        jql = f'project = {project_key} AND fixVersion = "{version_name}"'
         url = urljoin(self.config['jira_base_url'], "rest/api/2/search")
         
         try:
             response = self._make_request(
                 'GET',
                 url,
                 headers=self.headers,
                params={'jql': jql, 'fields': 'key,summary,status'},
                 timeout=30
             )
             
         else:
             print(f"Version {version_name} already exists (no issues assigned)")
 
    def create_versions_for_dates(self, project_key: str, dates: List[datetime], debug: bool = False, dry_run: bool = False, format_keys: Optional[List[str]] = None) -> None:
        """
        Create versions for a list of dates
         
         Args:
            project_key: Jira project key
            dates: List of dates to create versions for
            debug: If True, print debug information
            dry_run: If True, simulate the creation
            format_keys: Optional list of format keys to use instead of project defaults
             
        Raises:
            ValueError: If project_key is empty or dates is empty
            JiraApiError: If version creation fails
         """
         if not project_key or not dates:
             raise ValueError("Project key and dates are required")
             
         for date in dates:
            week_num = date.isocalendar()[1]
             for version_format in self.get_project_formats(project_key, format_keys):
                version_name = version_format.format(
                    project_key,
                    week_num,
                    date.year,
                    date.month,
                    date.day
                )
                 self.create_version(project_key, version_name, dry_run, debug)
 
     def create_custom_version(self, project_key: str, date_str: str, debug: bool = False, dry_run: bool = False, format_keys: Optional[List[str]] = None) -> None:
         versions = self.list_versions(project_key)
         return next((v for v in versions if v['name'] == version_name), None)
 
 def create_parser() -> argparse.ArgumentParser:
     """Create and configure the argument parser"""
     parser = argparse.ArgumentParser(
     list_parser.add_argument("project_key", help="Jira project key")
     list_parser.add_argument("--show-all", action="store_true", help="Show both released and unreleased versions")
     list_parser.add_argument("--show-released", action="store_true", help="Show only released versions")
     
     # Create command
     create_parser = subparsers.add_parser('create', help='Create new version(s)')
 
 def handle_list_command(manager: JiraVersionManager, args: argparse.Namespace) -> None:
     """Handle the list command"""
    versions = manager.list_versions(args.project_key)
    
    # Filter versions based on release status
    if not args.show_all:
        if args.show_released:
            versions = [v for v in versions if v.get('released', False)]
        else:
            versions = [v for v in versions if not v.get('released', False)]
    
    # Sort versions by release status and name
    versions.sort(key=lambda v: (v.get('released', False), v['name']))
    
    print(f"\nVersions for project {args.project_key}:")
    if not versions:
        status_type = "released" if args.show_released else "unreleased"
        print(f"No {status_type if not args.show_all else ''} versions found.")
        return
        
    for version in versions:
        status = "Released" if version.get('released', False) else "Unreleased"
        print(f"- {version['name']} ({status}) [ID: {version['id']}]")
 
 def handle_create_command(manager: JiraVersionManager, args: argparse.Namespace) -> None:
     """Handle the create command"""