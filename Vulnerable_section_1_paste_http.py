 import mimetypes
 import time
 
 import web, web.form, web.page
 
         try:
             alias = paste.put(alias, name, language, code)
 
            self.message = 'Successfully created at <a href="' + config.service + '/' + alias + '">' + config.service + '/' + alias + '</a>.'
         except KeyError:
             self.message = 'This alias already exists. Wait until it expires or choose another.'
 
         except:
             log.pastelog.exception()
 
            highlighted = code
 
         try:
             language_txt = mime.types[language]
         except KeyError:
             language_txt = 'Text'
 
        return page.format(pygments=pygments.formatters.HtmlFormatter().get_style_defs('.highlight'), name=name, date=date, expire=expire, language=language_txt, code=highlighted, raw=self.request.resource + '/raw')
 
 
 class Raw(web.HTTPHandler):