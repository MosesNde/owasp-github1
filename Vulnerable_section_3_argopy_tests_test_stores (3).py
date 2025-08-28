             with fs.open(uri, "r") as fp:
                 fp.read()
             assert isinstance(fs.cachepath(uri), str)
             # Now, we can clear the cache:
             fs.clear_cache()
             # And verify it does not exist anymore:
             with pytest.raises(CacheFileNotFound):
                 fs.cachepath(uri)
            os.remove(uri)
 
 
 @requires_connection
             fs.read_csv(uri, skiprows=8, header=0)
             assert isinstance(fs.cachepath(uri), str)
 
 
 class Test_IndexFilter_WMO:
     kwargs = [