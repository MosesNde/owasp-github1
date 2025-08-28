         'token': 'token',
         'printer': 'printer',
         '_print': 'print',
        'current_time': 'current_time',
        'time_left': 'time_left',
         'percent': 'percent',
         'image': 'image',
         'action': 'action'
             self.token = token
         if printer is not None:
             self.printer = printer
        self._print = _print
        self.current_time = current_time
        self.time_left = time_left
        self.percent = percent
         self.image = image
         if action is not None:
             self.action = action