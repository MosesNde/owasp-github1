 import tempfile
 import urllib.parse
 from pathlib import Path
from typing import Any
 
 from qubesbuilder.common import VerificationMode
 from qubesbuilder.component import QubesComponent
     pass
 
 
 class FetchPlugin(ComponentPlugin):
     """
     FetchPlugin manages generic fetch source
                 ]
             if file.get("uncompress", False):
                 download_cmd += ["--uncompress"]
            cmd = [" ".join(download_cmd)]
             try:
                 executor.run(cmd, copy_in, copy_out, environment=self.environment)
             except ExecutorError as e:
                         str(self.component.source_dir / pubkey),
                     ]
 
            cmd = [" ".join(verify_cmd)]
             try:
                 local_executor.run(cmd, copy_in, copy_out, environment=self.environment)
             except ExecutorError as e:
             (source_dir / "vtags", temp_dir),
         ]
         cmd = [
            f"rm -f {source_dir}/hash {source_dir}/vtags",
            f"cd {executor.get_builder_dir()}",
        ]
        cmd += [f"git -C {source_dir} rev-parse 'HEAD^{{}}' >> {source_dir}/hash"]
        cmd += [
            f"git -C {source_dir} tag --points-at HEAD --list 'v*' >> {source_dir}/vtags"
         ]
         try:
             executor.run(cmd, copy_in, copy_out, environment=self.environment)
         except ExecutorError as e:
         # Modules (formerly known as INCLUDED_SOURCES in Makefile.builder)
         modules = parameters.get("modules", [])
         if modules:

             # Get git module hashes
             copy_in = [
                 (self.component.source_dir, executor.get_builder_dir()),
             ]
             copy_out = [(source_dir / "modules", temp_dir)]
             cmd = [
                f"rm -f {source_dir}/modules",
                f"cd {executor.get_builder_dir()}",
             ]
             for module in modules:
                 cmd += [
                    f"git -C {source_dir}/{module} rev-parse HEAD >> {source_dir}/modules"
                 ]
             try:
                 executor.run(cmd, copy_in, copy_out, environment=self.environment)
                     ),
                 ]
                 cmd += [
                    f"{executor.get_plugins_dir()}/fetch/scripts/create-archive {source_dir}/{module['name']} {module['archive']} {module['name']}/",
                 ]
 
             try: