             libsvm.convert(self.libsvm_model, input_length=num_inputs - 1)
 
     def test_conversion_from_filesystem(self):
        libsvm_model_path = tempfile.mktemp(suffix="model.libsvm")
         svmutil.svm_save_model(libsvm_model_path, self.libsvm_model)
         spec = libsvm.convert(
             libsvm_model_path, input_names="data", target_name="target"