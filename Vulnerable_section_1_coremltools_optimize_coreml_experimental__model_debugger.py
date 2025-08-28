                 key: value for key, value in outputs.items() if key not in model_output_names
             }
 
            for output_name, output_value in outputs.items():
                 self.record_intermediate_output(output_value, output_name, activation_stats_dict)