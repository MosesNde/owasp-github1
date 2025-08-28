 
         om = self.runtime.omega
         nbname = self.jobname
         value = md5(uuid4().bytes).hexdigest()
         existing = ','.join(om.jobs.list(f'tasks/{nbname}*'))
         while True: