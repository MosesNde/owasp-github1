     printf( "Writing large array\n" );
     auto fid = AMP::openHDF5( "test_HDF5.large.hdf5", "w", AMP::Compression::GZIP );
     AMP::writeHDF5( fid, "data", data );
    AMP::closeHDF5( fid );
     NULL_USE( ut );
 }
 
     data.initialize();
     auto fid = AMP::openHDF5( "test_HDF5.hdf5", "w" );
     writeHDF5( fid, data );
    AMP::closeHDF5( fid );
 
     // Read the variables from HDF5
     data_struct data2;
     fid = AMP::openHDF5( "test_HDF5.hdf5", "r" );
     readHDF5( fid, data2 );
    AMP::closeHDF5( fid );
     checkResults( "readHDF5 (1): ", data, data2, ut );
 
    // Read the data using the class interface
     data_struct data3;
     fid = AMP::openHDF5( "test_HDF5.hdf5", "r" );
     readHDF52( fid, data3 );
    AMP::closeHDF5( fid );
    checkResults( "readHDF5 (2): ", data, data3, ut );
 
     // Test compression
     testCompression( ut );
     // Return
     data.clear();
     data2.clear();
    data3.clear();
     int N_errors = ut.NumFailGlobal();
     ut.report();
     ut.reset();