 	def create(self, dmg, volume_name, directory, symlinks):
 		input_size = sum(os.stat(os.path.join(path, f)).st_size for path, dirs, files in os.walk(directory) for f in files)
 		output_size = max(input_size * 2, 1024**2)
		hfs = tempfile.mktemp(prefix=dmg + '.', suffix='.hfs')
 		self._create_hfs(hfs, volume_name, output_size)
 		self._add(hfs, directory)
 		for target, link_name in symlinks: