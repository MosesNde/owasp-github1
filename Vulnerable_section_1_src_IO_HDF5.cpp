     // H5Pclose( pid );
     return fid;
 }
void closeHDF5( hid_t fid )
 {
     // Try to close any remaining objects (needed to ensure we can reopen the data if desired)
    hid_t file[1000], set[1000], group[1000], type[1000], attr[1000];
    size_t N_file  = H5Fget_obj_ids( fid, H5F_OBJ_FILE, 1000, file );
    size_t N_set   = H5Fget_obj_ids( fid, H5F_OBJ_DATASET, 1000, set );
    size_t N_group = H5Fget_obj_ids( fid, H5F_OBJ_GROUP, 1000, group );
    size_t N_type  = H5Fget_obj_ids( fid, H5F_OBJ_DATATYPE, 1000, type );
    size_t N_attr  = H5Fget_obj_ids( fid, H5F_OBJ_ATTR, 1000, attr );
    for ( size_t i = 0; i < N_file; i++ ) {
        if ( file[i] != fid )
            H5Fclose( file[i] );
     }
    for ( size_t i = 0; i < N_set; i++ )
        H5Dclose( set[i] );
    for ( size_t i = 0; i < N_group; i++ )
        H5Gclose( group[i] );
    for ( size_t i = 0; i < N_type; i++ )
        H5Tclose( type[i] );
    for ( size_t i = 0; i < N_attr; i++ )
        H5Aclose( attr[i] );
     // Flush the data (needed to ensure we can reopen the data if desired)
     unsigned intent;
     H5Fget_intent( fid, &intent );
 }
 
 
 /************************************************************************
  * Check if we support compression                                       *
  ************************************************************************/
     } else {
         AMP_ERROR( "Internal error" );
     }
     return compress;
 }
 
     hid_t dataset = H5Dopen2( fid, name.data(), H5P_DEFAULT );
     H5Eset_auto2( H5E_DEFAULT, func, client );
     bool exists = dataset > 0;
    // if ( exists )
    //    H5Dclose( dataset );
     return exists;
 }
 hid_t createGroup( hid_t fid, const std::string_view &name )
 {
     return H5Gcreate2( fid, name.data(), H5P_DEFAULT, H5P_DEFAULT, H5P_DEFAULT );
 }
 hid_t openGroup( hid_t fid, const std::string_view &name )
 {
     if ( !H5Gexists( fid, name ) )
         AMP_ERROR( "Group " + std::string( name ) + " does not exist" );
     return H5Gopen2( fid, name.data(), H5P_DEFAULT );
 #else // No HDF5
 // Dummy implementations for no HDF5
 hid_t openHDF5( const std::string_view &, const char *, AMP::Compression ) { return 0; }
void closeHDF5( hid_t ) {}
 bool H5Gexists( hid_t, const std::string_view & ) { return false; }
 bool H5Dexists( hid_t, const std::string_view & ) { return false; }
 hid_t createGroup( hid_t, const std::string_view & ) { return 0; }
 hid_t openGroup( hid_t, const std::string_view & ) { return 0; }
 void closeGroup( hid_t ) {}
 void writeHDF5( hid_t, const std::string_view &, size_t, const std::byte * );
 void readHDF5( hid_t, const std::string_view &, size_t, std::byte * );
 #endif
 
 } // namespace AMP