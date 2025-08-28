 
     def preprocess(self):
         self.preprocessor.preprocess()
        text = open(self.preprocess_output).read()
         os.remove(self.preprocess_output)
         return text
 