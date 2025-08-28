         xmlrpc_c::serverAbyss myAbyssServer(
             myRegistry,
             8080,              // TCP port on which to listen
            "/tmp/xmlrpc_log"  // Log file
             );
         
         myAbyssServer.run();