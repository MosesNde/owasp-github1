     def _clear_cache_item(self, uri):
         """ Open fsspec cache registry (pickle file) and remove entry for uri
 
            todo: Replace by the pop_from_cache fsspec method introduced in 0.7.4 in another PR
         """
         # See the "save_cache()" method in:
         # https://filesystem-spec.readthedocs.io/en/latest/_modules/fsspec/implementations/cached.html#WholeFileCacheFileSystem
                 cache[k] = v.copy()
             else:
                 os.remove(os.path.join(self.fs.storage[-1], v['fn']))
        fn2 = tempfile.mktemp()
        with open(fn2, "wb") as f:
             pickle.dump(cache, f)
        shutil.move(fn2, fn)
 
     def clear_cache(self):
         """ Remove cache files and entry from uri open with this store instance """
         if self.cache:
             for uri in self.cache_registry:
                 self._clear_cache_item(uri)
                # self.fs.pop_from_cache(uri)
 
     @abstractmethod
     def open_dataset(self, *args, **kwargs):
 
         """
         log.debug("Reading csv: %s" % url)
        try:
            with self.open(url) as of:
                df = pd.read_csv(of, **kwargs)
            return df
        except requests.HTTPError as e:
            self._verbose_exceptions(e)
 
     def open_json(self, url, **kwargs):
         """ Return a json from an url, or verbose errors
             return js
         except json.JSONDecodeError:
             raise
        except requests.HTTPError as e:
            self._verbose_exceptions(e)
 
     def _mfprocessor_json(self, url, preprocess=None, *args, **kwargs):
         # Load data