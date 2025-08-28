 import sys
 import threading
 import traceback
 from pathlib import Path
 from time import sleep
 
 
 
 # wait for vm to be up then connect and return qmp instance
 def qmp_connect(
     machine_name: str, vm: VmThread, flake_url: str | None = None
) -> QEMUMonitorProtocol:
     if flake_url is None:
         flake_url = str(Path.cwd())
     state_dir = vm_state_dir(flake_url, machine_name)
     wait_vm_up(machine_name, vm, flake_url)
    qmp = QEMUMonitorProtocol(
         address=str(os.path.realpath(state_dir / "qmp.sock")),
    )
    qmp.connect()
    return qmp
 
 
 # wait for vm to be up then connect and return qga instance
 def qga_connect(
     machine_name: str, vm: VmThread, flake_url: str | None = None
) -> QgaSession:
     if flake_url is None:
         flake_url = str(Path.cwd())
     state_dir = vm_state_dir(flake_url, machine_name)
     wait_vm_up(machine_name, vm, flake_url)
    return QgaSession(os.path.realpath(state_dir / "qga.sock"))