             pipeline = list(pipeline)[:-1]
         spipeline = json.dumps(pipeline, sort_keys=True)
         data = '{}_{}'.format(collection.name, spipeline).encode('utf-8')
         key = hashlib.md5(data).hexdigest()
         return key
 