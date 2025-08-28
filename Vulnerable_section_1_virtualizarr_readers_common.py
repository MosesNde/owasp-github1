     ).open_file()
 
     # TODO replace with only opening specific variables via `open_zarr(ManifestStore)` in #473
    loadable_ds = xr.open_dataset(
         fpath,  # type: ignore[arg-type]
         group=group,
         decode_times=decode_times,
    )

    var_names_to_load: list[Hashable]
    if isinstance(loadable_variables, list):
        var_names_to_load = list(loadable_variables)
    elif loadable_variables is None:
        # If `loadable_variables`` is None then we have to explicitly match default behaviour of xarray
        # i.e. load and create indexes only for dimension coordinate variables.
        # We already have all the indexes and variables we should be keeping - we just need to distinguish them.
        var_names_to_load = [
            name for name, var in loadable_ds.variables.items() if var.dims == (name,)
        ]
    else:
        raise ValueError(
            f"loadable_variables must be an iterable of string variable names, or None, but got type {type(loadable_variables)}"
         )
 
    # this will automatically keep any IndexVariables needed for loadable 1D coordinates
    loadable_var_names_to_drop = set(loadable_ds.variables).difference(
        var_names_to_load
    )
    ds_loadable_to_keep = loadable_ds.drop_vars(
        loadable_var_names_to_drop, errors="ignore"
    )

    ds_virtual_to_keep = fully_virtual_dataset.drop_vars(
        var_names_to_load, errors="ignore"
    )
 
    # we don't need `compat` or `join` kwargs here because there should be no variables with the same name in both datasets
    return xr.merge(
        [
            ds_loadable_to_keep,
            ds_virtual_to_keep,
        ],
    )
 
 
 # TODO this probably doesn't need to actually support indexes != {}