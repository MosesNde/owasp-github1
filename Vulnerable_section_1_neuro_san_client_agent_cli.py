         arg_parser.add_argument("--sly_data", type=str,
                                 help="JSON string containing data that is out-of-band to the chat stream, "
                                      "but is still essential to agent function")
        arg_parser.add_argument("--connection", default="service",
                                 choices=["service", "direct"],
                                 help="""
 The type of connection to initiate. Choices are to connect to: