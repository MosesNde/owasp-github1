     if (bindResult == SOCKET_ERROR)
     {
         const auto err = ::WSAGetLastError();
         throw std::runtime_error("Failed to bind socket: " + std::to_string(err));
     }
 
     // Listen
     if (::listen(handle, SOMAXCONN) == SOCKET_ERROR)
     {
        throw std::runtime_error("Failed to listen on socket: " + std::to_string(::WSAGetLastError()));
     }
 
     return { handle };
     if (connectResult == SOCKET_ERROR)
     {
         const auto err = ::WSAGetLastError();
         throw std::runtime_error("Failed to connect to server: " + std::to_string(err));
     }
 