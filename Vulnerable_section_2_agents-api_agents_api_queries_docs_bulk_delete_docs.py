 from ...autogen.openapi_model import BulkDeleteDocsRequest, ResourceDeletedResponse
 from ...common.utils.datetime import utcnow
 from ...common.utils.db_exceptions import common_db_exceptions
from ..utils import pg_query, rewrap_exceptions, wrap_in_class
 
 
 @rewrap_exceptions(common_db_exceptions("doc", ["delete"]))
     Deletes docs and their associated doc_owners entries for the given criteria.
     """
     metadata_filter = data.metadata_filter or {}
    params = [developer_id, owner_type, owner_id]

    # Build the metadata filter conditions
    metadata_conditions = ""
     delete_all = getattr(data, "delete_all", False)
 
     if not delete_all and not metadata_filter:
         """
         return query, []
 
    if not delete_all and metadata_filter:
        # Using parameterized queries properly to prevent SQL injection
        for key, value in metadata_filter.items():
            # Calculate the next parameter indices safely
            param_idx_key = len(params) + 1
            param_idx_value = len(params) + 2
            metadata_conditions += f" AND d.metadata->>${param_idx_key} = ${param_idx_value}"
            params.extend([key, value])
 
     query = f"""
     WITH deleted_docs AS (