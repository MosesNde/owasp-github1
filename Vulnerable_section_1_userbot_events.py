 
     def decorator(func):
         async def wrapper(check):
             if group_only and not check.is_group:
                 await check.respond("`Are you sure this is a group?`")
                 return