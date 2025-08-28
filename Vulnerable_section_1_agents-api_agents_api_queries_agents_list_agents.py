 
 from ...autogen.openapi_model import Agent
 from ...common.utils.db_exceptions import common_db_exceptions
from ..utils import pg_query, rewrap_exceptions, wrap_in_class
 
 # Define the raw SQL query
 raw_query = """
     if direction.lower() not in ["asc", "desc"]:
         raise HTTPException(status_code=400, detail="Invalid sort direction")
 
    # Build metadata filter clause if needed

    agent_query = raw_query.format(
        metadata_filter_query="AND metadata @> $6::jsonb" if metadata_filter else "",
    )

     params = [
         developer_id,
         limit,
         direction,
     ]
 
     if metadata_filter:
         params.append(metadata_filter)
 