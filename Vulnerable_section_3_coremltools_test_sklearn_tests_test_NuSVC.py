                 self.assertEqual(metrics["num_errors"], 0)
 
     def test_conversion_from_filesystem(self):
        libsvm_model_path = tempfile.mktemp(suffix="model.libsvm")
         svmutil.svm_save_model(libsvm_model_path, self.libsvm_model)
         spec = libsvm.convert(libsvm_model_path, "data", "target")
 