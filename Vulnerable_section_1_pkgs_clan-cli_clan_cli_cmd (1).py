         weakref.finalize(self, self.table_print)
 
     def table_print(self) -> None:
        if os.getenv("PERF") != "1":
            return
         print("======== CMD TIMETABLE ========")
 
         # Sort the table by time in descending order
             self.table[cmd] = time
 
 
TIME_TABLE = TimeTable()
 
 
 def run(
     tstart = datetime.datetime.now(tz=datetime.UTC)
 
     # Start the subprocess
    process = subprocess.Popen(
         cmd,
         cwd=str(cwd),
         env=env,
         stdout=subprocess.PIPE,
         stderr=subprocess.PIPE,
    )
    stdout_buf, stderr_buf = handle_output(process, log)
 
    if input:
        process.communicate(input)
    else:
        process.wait()
    tend = datetime.datetime.now(tz=datetime.UTC)
 
     global TIME_TABLE
    TIME_TABLE.add(shlex.join(cmd), tend - tstart)
 
     # Wait for the subprocess to finish
     cmd_out = CmdOut(