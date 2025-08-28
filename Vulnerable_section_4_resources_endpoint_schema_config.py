         input_dto_class=GetManyDataRequestsRequestsDTO,
     )
     DATA_REQUESTS_BY_ID_GET = EndpointSchemaConfig(
        input_schema=None, primary_output_schema=GetByIDDataRequestsResponseSchema()
     )
     DATA_REQUESTS_BY_ID_PUT = EndpointSchemaConfig(
         input_schema=DataRequestsPutSchema(),