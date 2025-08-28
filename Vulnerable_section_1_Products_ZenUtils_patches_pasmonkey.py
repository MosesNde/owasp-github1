         url = "%s/zenoss_terms/?came_from=%s" % (
                     self.absolute_url(), urllib.quote(came_from))
     else:
        url = came_from
 
     fragment = request.get('fragment', '')
     if fragment: