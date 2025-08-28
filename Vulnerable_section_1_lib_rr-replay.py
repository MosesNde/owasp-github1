 
 
 async def run_gdb(cmd):
    args = "".join([f'"{pipes.quote(a)}"' for a in sys.argv[1:]])
    gdb_proc = await asyncio.create_subprocess_shell(cmd + ' ' + args)
     await gdb_proc.communicate()
     return gdb_proc.returncode
 