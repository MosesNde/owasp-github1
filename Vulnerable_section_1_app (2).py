 import bleach
 import requests
 
service_version = "20241220.01"
 Welcome = 'Welcome to ref datacenter API server, version ' + service_version + ', indexer %s' % \
           Cfg.NETWORK[Cfg.NETWORK_ID]["INDEXER_HOST"][-3:]
 # Instantiation, which can be regarded as fixed format