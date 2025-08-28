             temp_dir = tempfile.mkdtemp()
             get_remote_file_to_local(os.path.join(remote_dir, "state.pkl"),
                                      os.path.join(temp_dir, "state.pkl"))
            import pickle
             with open(os.path.join(temp_dir, "state.pkl"), 'rb') as f:
                state_dicts = pickle.load(f)
         finally:
             shutil.rmtree(temp_dir)
         return state_dicts