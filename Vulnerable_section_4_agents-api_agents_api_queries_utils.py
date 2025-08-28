     if isinstance(data, list | tuple):
         return [serialize_model_data(item) for item in data]
     return data