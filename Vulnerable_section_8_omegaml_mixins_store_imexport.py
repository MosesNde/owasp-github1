             rmtree(self.path)
         self.manifest = self._read_manifest()
 
    def compress(self):
         # create a timestamped path that does not contain :
         # -- due to https://superuser.com/a/1720174
         dt = str(datetime.utcnow().isoformat()).replace(':', '')
        tfn = self.path.parent / f'{self.path.name}-{dt}.tgz'
         Path(tfn).unlink(missing_ok=True)
        with tarfile.open(tfn, 'w:gz') as tar:
             tar.add(self.path, arcname=self.path.name, recursive=True)
         self.clear()
         return tfn
 
    def decompress(self):
         if self.path.is_file():
            target = self.path.parent / self.path.name.replace('.tgz', '')
            with tarfile.open(self.path, 'r:gz') as tar:
                tar.extractall(target)
             # the first entry in the archive is the actual archive contents
             basename = list(target.iterdir())[0]
             arc = self.__class__(basename, self.store)
         self.omega = omega
 
     def to_archive(self, path, objects=None, fmt='omega', compress=False, progressfn=None):
         obj: Metadata | str
         store: ObjectImportExportMixin | OmegaStore
         if not objects:
             objects = self.omega.list(raw=True)
         with OmegaExporter.archive(path, fmt=fmt) as arc:
             arc.clear()
             for obj in objects:
                progressfn(obj) if progressfn else None
                 if isinstance(obj, Metadata):
                     store = self.omega.store_by_meta(obj)
                     store.to_archive(obj.name, arc)
                     for objname in objects:
                         store.to_archive(objname, arc)
         if compress:
            archive_path = arc.compress()
         else:
             archive_path = path
         return archive_path