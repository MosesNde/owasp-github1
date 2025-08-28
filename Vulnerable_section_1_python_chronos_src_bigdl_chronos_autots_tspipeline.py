 
         :param file_path: the folder location to save the pipeline
         '''
        import pickle
         if not os.path.isdir(file_path):
             os.mkdir(file_path)
         model_init_path = os.path.join(file_path, DEFAULT_MODEL_INIT_DIR)
         data_process = {"scaler": self._scaler,
                         "scaler_index": self._scaler_index}
         with open(model_init_path, "wb") as f:
            pickle.dump(model_init, f)
         with open(data_process_path, "wb") as f:
            pickle.dump(data_process, f)
         with open(best_config_path, "wb") as f:
            pickle.dump(self._best_config, f)
         # self._best_model.save(model_path)
         torch.save(self._best_model.model.state_dict(), model_path)
 
 
         :param file_path: the folder location to load the pipeline
         '''
        import pickle
         model_init_path = os.path.join(file_path, DEFAULT_MODEL_INIT_DIR)
         model_path = os.path.join(file_path, DEFAULT_BEST_MODEL_DIR)
         data_process_path = os.path.join(file_path, DEFAULT_DATA_PROCESS_DIR)
         best_config_path = os.path.join(file_path, DEFAULT_BEST_CONFIG_DIR)
         with open(model_init_path, "rb") as f:
            model_init = pickle.load(f)
         with open(data_process_path, "rb") as f:
            data_process = pickle.load(f)
         with open(best_config_path, "rb") as f:
            best_config = pickle.load(f)
 
         model_creator = model_init["model_creator"]
         optimizer_creator = model_init["optimizer_creator"]