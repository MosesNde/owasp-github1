         model = MLModel(self.spec)
         self.assertIsNotNone(model)
 
        filename = tempfile.mktemp(suffix=".mlmodel")
         save_spec(self.spec, filename)
         model = MLModel(filename)
         self.assertIsNotNone(model)
         model = MLModel(self.spec)
         self.assertIsNotNone(model)
 
        filename = tempfile.mktemp(suffix="")
         save_spec(self.spec, filename) # appends .mlmodel extension when it is not provided
         self.assertFalse(os.path.exists(filename))
 
         model.output_description["output"] = "This is output"
         self.assertEqual(model.output_description["output"], "This is output")
 
        filename = tempfile.mktemp(suffix=".mlmodel")
         model.save(filename)
         loaded_model = MLModel(filename)
 
     )
     def test_future_version(self):
         self.spec.specificationVersion = 10000
        filename = tempfile.mktemp(suffix=".mlmodel")
         save_spec(self.spec, filename, auto_set_specification_version=False)
         model = MLModel(filename)
         # this model should exist, but throw an exception when we try to use
 
         # manually set a high specification version
         self.spec.specificationVersion = 4
        filename = tempfile.mktemp(suffix=".mlmodel")
         save_spec(self.spec, filename, auto_set_specification_version=True)
         model = MLModel(filename)
         assert model.get_spec().specificationVersion == 1
         # set a high specification version
         builder.spec.specificationVersion = 3
         model = MLModel(builder.spec)
        filename = tempfile.mktemp(suffix=".mlmodel")
         model.save(filename)
         # load the model back
         model = MLModel(filename)
         assert model.get_spec().specificationVersion == 1
 
         # test save without automatic set specification version
         self.spec.specificationVersion = 3
        filename = tempfile.mktemp(suffix=".mlmodel")
         save_spec(self.spec, filename, auto_set_specification_version=False)
         model = MLModel(filename)
         # the specification version should be original