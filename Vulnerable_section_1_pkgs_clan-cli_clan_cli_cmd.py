 import timeit
 import weakref
 from collections.abc import Iterator
from contextlib import contextmanager
 from enum import Enum
 from pathlib import Path
 from typing import IO, Any
             pass
 
 
 class TimeTable:
     """
     This class is used to store the time taken by each command
         logger.debug(f"$: {shlex.join(cmd)} \nCaller: {get_caller()}")
     start = timeit.default_timer()
 
    # Start the subprocess
    with (
        subprocess.Popen(
            cmd,
            cwd=str(cwd),
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            start_new_session=not needs_user_terminal,
        ) as process,
        terminate_process_group(process)
        if not needs_user_terminal
        else contextlib.suppress(),  # NOQA: B022
    ):
         stdout_buf, stderr_buf = handle_output(process, log)
 
         if input: