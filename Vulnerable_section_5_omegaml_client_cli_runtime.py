         qualifier = om.runtime.auth.qualifier
         auth = requests.auth.HTTPBasicAuth(user, om.runtime.auth.apikey)
         headers = {'Qualifier': qualifier}
         appsurl = ensure_api_url(apphub_url, om.defaults, key='OMEGA_APPHUB_URL')
         name = name.replace('apps/', '')
         stop = requests.get(f'{appsurl}/apps/api/stop/{user}/{name}'.format(om.runtime.auth.userid),