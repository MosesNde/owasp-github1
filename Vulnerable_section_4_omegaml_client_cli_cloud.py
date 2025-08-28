 import pandas as pd
 import requests
 import subprocess
 from omegaml.client.auth import AuthenticationEnv
 from omegaml.client.docoptparser import CommandBase
 from omegaml.client.util import get_omega
 
 
 class CloudCommandBase(CommandBase):
             url = resp.headers['Location']
             if not url.startswith(restapi_url):
                 url = f'{restapi_url}{url}'
            resp = requests.get(url, auth=auth)
            resp.raise_for_status()
         return resp.json()
 
     def _wait_service_command(self, om, command):
         nowdt = datetime.utcnow().isoformat()
         mongo_url = mongoshim.mongo_url(om)
         path = archive or f'{userid}-{nowdt}.mongodump.archive'
        dump_cmd = f'mongodump --uri {mongo_url} --gzip --archive={path} {options}'
        restore_cmd = f'mongorestore --uri {mongo_url} --gzip --archive={path} --drop {options}'
         cmd = dump_cmd if backup else restore_cmd
         if restore:
             answer = self.ask(f"Are you sure to restore to {mongo_url} from {path}?", options="Yes,No")