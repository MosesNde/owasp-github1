 import tldextract
 import logging
 import shutil
 
 from threading import Thread
 
 def get_cms_details(url):
     # this function will fetch cms details using cms_detector
     response = {}
    cms_detector_command = 'python3 /usr/src/github/CMSeeK/cmseek.py -u {} --random-agent --batch --follow-redirect'.format(url)
    os.system(cms_detector_command)
 
     response['status'] = False
     response['message'] = 'Could not detect CMS!'