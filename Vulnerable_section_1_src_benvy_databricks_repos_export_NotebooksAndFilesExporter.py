 import json
 import shutil
 import tempfile
 from typing import List
 from zipfile import ZipFile, ZIP_DEFLATED
 from databricks_cli.workspace.api import WorkspaceApi
         if self._dbc_content:
             return self._dbc_content
 
        dbc_temp_file = tempfile.mktemp()
 
         self._workspace_api.export_workspace(workspace_path, dbc_temp_file, fmt="DBC", is_overwrite=True)
 