         self._outf.close()
 
         if self._args.version and None == self._versionScript:
            cmd = "'%(lcov)s' -a '%(info)s' -o '%(info)s' --version-script '%(vers)s' %(checksum)s--rc compute_file_version=1 --branch-coverage --ignore inconsistent" % {
                'lcov': os.path.join(os.path.split(sys.argv[0])[0], 'lcov'),
                'checksum': "--checksum " if self._args.checksum else '',
                'info': self._args.output,
                'vers' : self._args.version,
            }
             try:
                x = subprocess.run(cmd, shell=True, check=True, stdout=True, stderr=True)
             except subprocess.CalledProcessError as err:
                 print("Error during lcov version append operation: %s" % (
                     str(err)))