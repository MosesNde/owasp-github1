             # but there is some prefix to the path that was already
             # trimmed by the routing
             if not self.request.path.endswith("/"):
                 self.redirect(self.request.path + "/", permanent=True)
                 return None
             absolute_path = os.path.join(absolute_path, self.default_filename)