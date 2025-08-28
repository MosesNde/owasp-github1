     
     id = str(uuid.uuid4())
     try:
        proc = await asyncio.create_subprocess_shell(
            f"git clone --depth=1 {repo_url} ../tmp/{id}",
             stdout=asyncio.subprocess.PIPE,
             stderr=asyncio.subprocess.PIPE,
         )
     if max_size != 10240:
         cmd += f" --max-size {max_size}"
 
    proc = await asyncio.create_subprocess_shell(
        cmd,
         stdout=asyncio.subprocess.PIPE,
         stderr=asyncio.subprocess.PIPE,
     )