 import re
 import shutil
 import subprocess
 from pathlib import Path, PurePath
from typing import List, Tuple, Union
 
 from qubesbuilder.common import sanitize_line, str_to_bool
 from qubesbuilder.executors import Executor, ExecutorError
 log = get_logger("executor:qubes")
 
 
 class QubesExecutor(Executor):
     def __init__(self, dispvm: str = "dom0", clean: Union[str, bool] = True, **kwargs):
         self._dispvm = dispvm
         src = source_path.expanduser().resolve()
         dst = destination_dir
         # FIXME: Refactor the qvm-run and qrexec commandlines.
        prepare_incoming_and_destination = [
            "/usr/bin/qvm-run-vm",
             vm,
            f"bash -c 'rm -rf {self.get_builder_dir()}/incoming/{src.name} {dst.as_posix()}/{src.name}'",
        ]
         copy_to_incoming = [
             "/usr/lib/qubes/qrexec-client-vm",
             vm,
             "qubesbuilder.FileCopyIn",
             "/usr/lib/qubes/qfile-agent",
             str(src),
         ]
        move_to_destination = [
            "/usr/bin/qvm-run-vm",
             vm,
            f"bash -c 'mkdir -p {dst.as_posix()} && mv {self.get_builder_dir()}/incoming/{src.name} {dst.as_posix()}'",
        ]
         try:
             log.debug(f"copy-in (cmd): {' '.join(prepare_incoming_and_destination)}")
             subprocess.run(prepare_incoming_and_destination, check=True)
         no_fail_copy_out_allowed_patterns=None,
         dig_holes: bool = False,
     ):

         dispvm = None
         try:
             result = subprocess.run(
                ["qrexec-client-vm", self._dispvm, "admin.vm.CreateDisposable"],
                 capture_output=True,
                 stdin=subprocess.DEVNULL,
             )
            dispvm = result.stdout.decode("utf8").replace("0\x00", "")
            if not re.match(r"disp[0-9]{1,4}", dispvm):
                 raise ExecutorError("Failed to create disposable qube.")
 
             # Adjust log namespace
             log.name = f"executor:qubes:{dispvm}"
 
             # Start the DispVM by running creation of builder directory
            start_cmd = [
                "/usr/bin/qvm-run-vm",
                 dispvm,
                f"bash -c 'sudo mkdir -p {self.get_builder_dir()} {self.get_builder_dir()} "
                f"{self.get_builder_dir()/'build'} {self.get_builder_dir()/'plugins'} "
                f"{self.get_builder_dir()/'distfiles'} "
                f"&& sudo chown -R {self.get_user()}:{self.get_group()} {self.get_builder_dir()}'",
            ]
             subprocess.run(start_cmd, stdin=subprocess.DEVNULL)
 
             # copy-in hook
                     self.replace_placeholders(str(f))
                     for f in files_inside_executor_with_placeholders
                 ]
                sed_cmd = [
                    f"sed -i 's#@BUILDER_DIR@#{self.get_builder_dir()}#g' {' '.join(files)}"
                ]
                if sed_cmd:
                    sed_cmd = [c.replace("'", "'\\''") for c in sed_cmd]
                    sed_cmd = [
                        "/usr/bin/qvm-run-vm",
                        dispvm,
                        f'bash -c \'{" && ".join(sed_cmd)}\'',
                     ]
                    subprocess.run(sed_cmd, stdin=subprocess.DEVNULL)
 
             bash_env = []
             if environment:
                 for key, val in environment.items():
                    bash_env.append(f"{str(key)}='{str(val)}'")
 
            cmd = [c.replace("'", "'\\''") for c in cmd]
            qvm_run_cmd = [
                "/usr/bin/qvm-run-vm",
                 dispvm,
                f'env {" ".join(bash_env)} bash -c \'{" && ".join(cmd)}\'',
            ]
 
             log.info(f"Executing '{' '.join(qvm_run_cmd)}'.")
 
             # Kill the DispVM to prevent hanging for while
             if dispvm and self._clean:
                 subprocess.run(
                    ["qrexec-client-vm", dispvm, "admin.vm.Kill"],
                     stdin=subprocess.DEVNULL,
                     stdout=subprocess.DEVNULL,
                 )