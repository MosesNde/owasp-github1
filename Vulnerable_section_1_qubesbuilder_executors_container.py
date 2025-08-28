 from pathlib import Path, PurePath
 import tempfile
 from typing import List, Tuple, Union
 
 from qubesbuilder.common import sanitize_line, str_to_bool
 from qubesbuilder.executors import Executor, ExecutorError
 
                 # fix permissions and user group
                 permissions_cmd = [
                    f"sudo mkdir -p {self.get_builder_dir()} {self.get_builder_dir()/'build'} {self.get_builder_dir()/'plugins'} {self.get_builder_dir()/'distfiles'}",
                    f"sudo chown -R {self._user}:{self._group} {self.get_builder_dir()}",
                 ]
 
                 # replace placeholders