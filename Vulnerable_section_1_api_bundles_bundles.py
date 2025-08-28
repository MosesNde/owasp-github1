 
 @router.get("/bundles", response_model_exclude_none=True)
 async def list_bundles(
     archived: bool = Query(False, description="Include archived bundles"),
 ) -> ListBundleModel:
     result: list[BundleModel] = []