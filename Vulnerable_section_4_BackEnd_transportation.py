         self.paths = []
 
     @abstractmethod
    def create_path(self):
         pass
 
     @abstractmethod
    def create_time(self):
         pass
 
     @abstractmethod
    def create_cost(self):
         pass
 
     def create(self):
         try:
            self.create_path()
            self.create_time()
            self.create_cost()
         except Exception as e:
             self.paths = []
             print(e)