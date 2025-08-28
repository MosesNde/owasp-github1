     namespace: Namespace,
     schema: SchemaTypes,
     model_name: Optional[str] = None,
):
     """
     Takes a Marshmallow schema class with custom arguments and
     returns a Flask-RESTX model and Request Parser for Restx documentation, correlating to the schema