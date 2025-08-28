 def _get_error_recode_polygons(in_file):
     ds_in = ogr.Open(in_file)
     layer_in = ds_in.GetLayer()
    out_file = tempfile.mktemp(suffix=".geojson")
    print(out_file)
    out_ds = ogr.GetDriverByName("GeoJSON").CreateDataSource(out_file)
    layer_out = out_ds.CopyLayer(layer_in, "error_recode")
    del layer_out
    del out_ds
    with open(out_file) as f:
        polys = ErrorRecodePolygons.Schema().load(json.load(f))
     return polys
 
 