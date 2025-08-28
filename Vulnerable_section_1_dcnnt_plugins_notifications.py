 import logging
 import subprocess
 
 from .base import Plugin
 from ..common import *
                         except Exception as e:
                             self.log(e, logging.WARNING)
                     icon = icon_path if icon_data else ''
                    command = cmd.format(uin=uin, name=name, icon=icon, text=text, title=title, package=package)
                     self.log('Execute: "{}"'.format(command))
                     subprocess.call(command, shell=True)