 from setuptools import setup, find_packages
 import os
 import json
 
 # Sample configuration that will be created
 SAMPLE_CONFIG = {
     "jira_base_url": "https://your-jira-instance.com",
     "jira_api_token": "your-api-token",
     "project_keys": ["PROJECT1", "PROJECT2", "PROJECT3"],
     "version_formats": {
        "standard": "{}.W{:02d}.{}.{:02d}.{:02d}",         # Default format
        "intake": "{}.INTAKE.W{:02d}.{}.{:02d}.{:02d}",    # Custom format with INTAKE prefix
        "release": "{}.RELEASE.{}.{:02d}.{:02d}"           # Custom format for releases
     },
     "project_formats": {
        "PROJECT1": ["standard", "release"],  # Uses both standard and release formats
        "PROJECT2": ["intake"],               # Uses only intake format
        # PROJECT3 not specified - will use standard format by default
     },
     "jira_verify_ssl": True
 }
 
 def create_sample_config():
     """Create sample configuration file if it doesn't exist"""
    config_file = os.path.expanduser("~/.jira_version_manager.json")
     if not os.path.exists(config_file):
        with open(config_file, 'w') as f:
             json.dump(SAMPLE_CONFIG, f, indent=4)
         print(f"Created sample configuration file at {config_file}")
 
 setup(
     name="jira-version-manager",
     version="0.1.0",
     packages=find_packages(),
     install_requires=[
         "requests>=2.32.0",
        "urllib3>=2.0.0"
     ],
     extras_require={
         "dev": [
     author="Piotr Szmitkowski",
     author_email="pszmitkowski@gmail.com",
     description="A tool to manage Jira versions with support for custom formats and SSL verification",
    long_description=open("README.md").read(),
     long_description_content_type="text/markdown",
     keywords="jira, version management, agile",
    url="https://github.com/pszmitkowski/jira-version-manager",
     classifiers=[
         "Development Status :: 4 - Beta",
         "Intended Audience :: Developers",