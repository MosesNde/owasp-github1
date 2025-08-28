 import re
 
 from notebook.base.handlers import path_regex
 
 # build regexps that tornado uses:
 path_pat = re.compile('^' + '/x%s' % path_regex + '$')
 
 def test_path_regex():
     for path in (
         '/x',
         '/y/x/foo',
     ):
         assert not re.match(path_pat, path)