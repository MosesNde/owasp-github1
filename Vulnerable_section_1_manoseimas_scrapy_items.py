     project_name = Field()
     project_number = Field()
     project_url = Field()
    date = Field(input_processor=processor.Identity(),
                 output_processor=processor.TakeFirst())
     source = Field(input_processor=processor.Identity(),
                    output_processor=processor.TakeFirst())
 