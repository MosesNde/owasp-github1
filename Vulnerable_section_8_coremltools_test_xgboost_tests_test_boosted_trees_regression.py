         output_name = "target"
         feature_names = self.feature_names
 
        xgb_model_json = tempfile.mktemp("tree_model.json")
         xgb_json_out = self.xgb_model.get_dump(dump_format="json")
         with open(xgb_model_json, "w") as f:
             json.dump(xgb_json_out, f)