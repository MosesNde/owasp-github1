         application_id = algolia_application_id
 
     # Build the search request
    search_request = {
        "requests": [
            {
                "indexName": arguments.index_name,
                "query": arguments.query,
                "hitsPerPage": arguments.hits_per_page,
                "attributesToRetrieve": arguments.attributes_to_retrieve or [],
            }
        ]
     }
 
     # Initialize the Algolia client
     async with SearchClient(application_id, api_key) as client:
         result = json.loads((await client.search(search_request)).to_json())