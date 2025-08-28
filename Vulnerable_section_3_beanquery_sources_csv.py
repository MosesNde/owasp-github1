             converter = _TYPES_TO_PARSERS.get(ctype, ctype)
             self.columns[cname] = Column(len(self.columns), ctype, converter)
 
     def __iter__(self):
         self.data.seek(0)
         it = iter(self.reader)