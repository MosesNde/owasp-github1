         output_name = "target"
         feature_names = self.scikit_data["feature_names"]
 
        xgb_model_json = tempfile.mktemp("xgb_tree_model_classifier.json")
         xgb_json_out = self.xgb_model.get_dump(with_stats=True, dump_format="json")
         with open(xgb_model_json, "w") as f:
             json.dump(xgb_json_out, f)