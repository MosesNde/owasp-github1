         self.start_command = list(filter(lambda a: a != '', [tmp_file_starter, self.tmp_file]))
 
     def add_download(self, magnet: str):
         self.script += self.script_line.format(magnet)
 
     def flush_script(self):