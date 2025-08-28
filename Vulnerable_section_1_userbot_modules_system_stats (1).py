 #
 """ Userbot module for getting information about the server. """
 
from asyncio import create_subprocess_shell as asyncrunapp
 from asyncio.subprocess import PIPE as asyncPIPE
 from platform import python_version, uname
 from shutil import which
         await sysd.edit("`sysd Commad isn't permitted on channels`")
         return
     """ For .sysd command, get system info using neofetch. """
    try:
        neo = "neofetch --stdout"
        fetch = await asyncrunapp(
            neo,
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )
 
        stdout, stderr = await fetch.communicate()
        result = str(stdout.decode().strip()) \
            + str(stderr.decode().strip())
 
        await sysd.edit("`" + result + "`")
    except FileNotFoundError:
        await sysd.edit("`Install neofetch first !!`")
 
 
 @register(outgoing=True, pattern="^.botver$")
         await event.edit(
             "Shame that you don't have git, You're running 5.0 - 'Extended' anyway"
         )
 
 
 @register(outgoing=True, pattern="^.pip(?: |$)(.*)")
         await pip.edit("`pip Commad isn't permitted on channels`")
         return
     """ For .pip command, do a pip search. """
    pipmodule = pip.pattern_match.group(1)
    if pipmodule:
        await pip.edit("`Searching . . .`")
        invokepip = f"pip3 search {pipmodule}"
        pipc = await asyncrunapp(
            invokepip,
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )

        stdout, stderr = await pipc.communicate()
        pipout = str(stdout.decode().strip()) \
            + str(stderr.decode().strip())

        if pipout:
            if len(pipout) > 4096:
                await pip.edit("`Output too large, sending as file`")
                file = open("output.txt", "w+")
                file.write(pipout)
                file.close()
                await pip.client.send_file(
                    pip.chat_id,
                    "output.txt",
                    reply_to=pip.id,
                )
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
 
 
 @register(outgoing=True, pattern=r"^\.(?:live|on)\s?(.)?")