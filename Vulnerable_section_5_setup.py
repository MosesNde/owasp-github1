 import os
 import json
 from appdirs import user_data_dir

# Sample configuration that will be created
SAMPLE_CONFIG = {
    "jira_base_url": "https://your-jira-instance.com",
    "jira_api_token": "your-api-token",
    "project_keys": ["PROJECT1", "PROJECT2", "PROJECT3"],
    "version_formats": {
        "standard": "{PROJECT}.W{WEEK:02d}.{YEAR}.{MONTH:02d}.{DAY:02d}",         # Default format
        "intake": "{PROJECT}.INTAKE.W{WEEK:02d}.{YEAR}.{MONTH:02d}.{DAY:02d}",    # Custom format with INTAKE prefix
        "release": "{PROJECT}.{YEAR}.{MONTH:02d}.{DAY:02d}.RELEASE"               # Custom format for releases
    },
    "project_formats": {
        "default": ["standard"],                # Default format for all projects
        "PROJECT1": ["standard", "release"],    # Uses both standard and release formats
        "PROJECT2": ["intake"]                  # Uses only intake format
    },
    "issue_types": {
        "default": ["Epic"],                    # Default to show only Epics
        "PROJECT1": ["Epic", "Story"],          # Show Epics and Stories for PROJECT1
        "PROJECT2": ["Epic", "Task"]            # Show Epics and Tasks for PROJECT2
    },
    "release_days": {
        "default": [0, 1, 2, 3],               # Monday to Thursday by default
        "PROJECT1": {
            "days": [0, 2, 4],                 # Monday, Wednesday, Friday
            "frequency": 1                      # Every week (use 2 for every two weeks)
        }
    },
    "jira_verify_ssl": True
}

def create_sample_config():
    """Create sample configuration file if it doesn't exist"""
    config_dir = user_data_dir("jira-version-manager", "1500100xyz")
    config_file = os.path.join(config_dir, "config.json")
    
    if not os.path.exists(config_dir):
        os.makedirs(config_dir, mode=0o700)
        
    if not os.path.exists(config_file):
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(SAMPLE_CONFIG, f, indent=4)
        print(f"Created sample configuration file at {config_file}")
 
 def get_long_description():
     filename = os.path.join(os.path.dirname(__file__), "README.md")
 
 setup(
     name="jira-version-manager",
    version="0.1.0",
     packages=find_packages(),
     install_requires=[
         "requests>=2.32.0",
         "dev": [
             "pytest>=7.0.0",
             "pytest-cov>=4.0.0",
            "flake8>=6.0.0",
             "black>=24.0.0",
            "mypy>=1.0.0",
            "types-requests>=2.31.0",
            "types-urllib3>=2.0.0"
         ]
     },
     entry_points={
         "console_scripts": [
             "jira-version-manager=jira_version_manager.version_manager:main"
         ]
     },
    author="Piotr Szmitkowski",
    author_email="pszmitkowski@gmail.com",
     description="A tool to manage Jira versions with support for custom formats and SSL verification",
     long_description=get_long_description(),
     long_description_content_type="text/markdown",
     python_requires=">=3.8"
 )
 
# Create sample configuration file during installation
 if __name__ == "__main__":
    create_sample_config() 
\ No newline at end of file
\ No newline at end of file