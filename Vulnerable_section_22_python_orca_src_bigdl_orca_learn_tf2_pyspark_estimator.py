                 temp_dir = tempfile.mkdtemp()
                 get_remote_file_to_local(os.path.join(self.model_dir, "state.pkl"),
                                          os.path.join(temp_dir, "state.pkl"))
                import pickle
                 with open(os.path.join(temp_dir, "state.pkl"), 'rb') as f:
                    state = pickle.load(f)
                     self.model_weights = state['weights']
             finally:
                 shutil.rmtree(temp_dir)