 
             await sysd.edit("`" + result + "`")
         except FileNotFoundError:
            await sysd.edit("`Hella install neofetch first kthx`")
 
 
 @register(outgoing=True, pattern="^.botver$")
                              "` \n"
                              "`Revision: "
                              f"{revout}"
                             "` \n"
                             "`OpenUserBot Version: 7.7.7`")
         else:
             await event.edit(
                "Shame that you don't have Git, you're running v1.0 anyway!")
 
 
 @register(outgoing=True, pattern="^.pip(?: |$)(.*)")
                     remove("output.txt")
                     return
                 await pip.edit("**Query: **\n`"
                               f"{invokepip}"
                                "`\n**Result: **\n`"
                                f"{pipout}"
                                "`")
             else:
                 await pip.edit("**Query: **\n`"
                               f"{invokepip}"
                                "`\n**Result: **\n`No Result Returned/False`")
         else:
             await pip.edit("`Use .help pip to see an example`")
            
 
 @register(outgoing=True, pattern="^.alive$")
 async def amireallyalive(alive):