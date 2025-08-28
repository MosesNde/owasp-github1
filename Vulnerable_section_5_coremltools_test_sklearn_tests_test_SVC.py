                 break
 
     def test_conversion_from_filesystem(self):
        libsvm_model_path = tempfile.mktemp(suffix="model.libsvm")
         svmutil.svm_save_model(libsvm_model_path, self.libsvm_model)
         # libsvm's save(...) truncates floating points. So it's not going to match self.libsvm_model any more.
         spec = libsvm.convert(libsvm_model_path, self.column_names, "target")