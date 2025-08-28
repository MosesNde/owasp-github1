 #
 """ Userbot module for getting information about the server. """
 
from asyncio import create_subprocess_shell as asyncrunapp
 from asyncio.subprocess import PIPE as asyncPIPE
 from os import remove
 from platform import python_version, uname
     """ For .sysd command, get system info using neofetch. """
     if not sysd.text[0].isalpha() and sysd.text[0] not in ("/", "#", "@", "!"):
         try:
            neo = "neofetch --stdout"
             fetch = await asyncrunapp(
                neo,
                 stdout=asyncPIPE,
                 stderr=asyncPIPE,
             )
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@",
                                                              "!"):
         if which("git") is not None:
            invokever = "git describe --all --long"
             ver = await asyncrunapp(
                invokever,
                 stdout=asyncPIPE,
                 stderr=asyncPIPE,
             )
             stdout, stderr = await ver.communicate()
             verout = str(stdout.decode().strip()) \
                 + str(stderr.decode().strip())
 
            invokerev = "git rev-list --all --count"
             rev = await asyncrunapp(
                invokerev,
                 stdout=asyncPIPE,
                 stderr=asyncPIPE,
             )
         pipmodule = pip.pattern_match.group(1)
         if pipmodule:
             await pip.edit("`Searching . . .`")
            invokepip = f"pip3 search {pipmodule}"
             pipc = await asyncrunapp(
                invokepip,
                 stdout=asyncPIPE,
                 stderr=asyncPIPE,
             )