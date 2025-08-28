             link["link"] = entry.summary.split('href="')[2].split('"')[0]
         except IndexError:
             link["link"] = entry.link

         try:
             publish_date = entry.published_parsed
         except AttributeError:
     def follow_old(self):
         for link in Link.objects.all():
             try:
                link = self.follow_redirects(link.link)
             except Exception as e:
                 print "%s - skipping %s" % (e, link.link)
             else:
                Link.objects.filter(id=link.id).update(link=link)