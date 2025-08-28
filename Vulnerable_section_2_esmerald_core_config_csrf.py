 from pydantic import BaseModel
 from typing_extensions import Annotated, Doc, Literal
 
from esmerald.types import HTTPMethod

 
 class CSRFConfig(BaseModel):
     """
         ),
     ] = None
     safe_methods: Annotated[
        Set[HTTPMethod],
         Doc(
             """
             A set of allowed safe methods that can set the cookie.