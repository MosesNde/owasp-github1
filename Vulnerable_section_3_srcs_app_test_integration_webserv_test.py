 import subprocess
 import tempfile
 import time
 
 TMP_WEBSERV_DIR = '/tmp/webserv/'
 PROJ_DIR = str(Path(__file__).parents[4])
         fp.write(os.urandom(90000000))
         yield fp
 
 def test_get_autoindex_200():
     url = 'http://localhost:8080'
     response = requests.get(url)
     assert response.status_code == 200
 
 def test_get_404():
    url = 'http://localhost:8080/invalidpath'
     response = requests.get(url)
     assert response.status_code == 404
 
     filepath = TMP_UPLOAD_DIR + filename
     assert filecmp.cmp(filepath, tmp_file.name)
     os.remove(filepath)