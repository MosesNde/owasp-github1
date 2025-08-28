 
 from ...autogen.openapi_model import Doc
 from ...common.utils.db_exceptions import common_db_exceptions
from ..utils import pg_query, rewrap_exceptions, wrap_in_class
 from .utils import transform_doc
 
 # Base query for listing docs with aggregated content and embeddings
     query = base_docs_query
     params = [developer_id, include_without_embeddings, owner_type, owner_id]
 
    # Add metadata filtering before GROUP BY
    if metadata_filter:
        for key, value in metadata_filter.items():
            query += f" AND d.metadata->>${len(params) + 1} = ${len(params) + 2}"
            params.extend([key, value])
 
     # Add GROUP BY clause
     query += """