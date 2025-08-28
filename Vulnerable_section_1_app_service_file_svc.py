         self.plugins = plugins
         self.exfil_dir = exfil_dir
         self.log = self.add_service('file_svc', self)
 
     async def download(self, request):
         """
 
     async def _get_file(self, name, platform):
         if name.endswith('.go'):
            name = await self._go_compile(name, platform)
             _, file_path = await self.find_file_path(name, location='payloads')
             with open(file_path, 'rb') as file_stream:
                 return name, file_stream.read()
         raise FileNotFoundError
 
     async def _go_compile(self, name, platform):
        if name.endswith('.go'):
            if which('go') is not None:
                plugin, file_path = await self.find_file_path(name)
                await self._change_file_hash(file_path)
                output = 'plugins/%s/payloads/%s-%s' % (plugin, name, platform)
                os.system('GOOS=%s go build -o %s -ldflags="-s -w" %s' % (platform, output, file_path))
                self.log.debug('%s compiled for %s with MD5=%s' %
                               (name, platform, md5(open(output, 'rb').read()).hexdigest()))
            return '%s-%s' % (name, platform)
        return name
 
     @staticmethod
     async def _change_file_hash(file_path, size=30):