             validation_schema=EntryDataRequestSchema,
         )
 

 class TypeaheadQuerySchema(Schema):
     query = fields.Str(
         required=True,