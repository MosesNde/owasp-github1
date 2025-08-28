 
 void RequestHandler::CheckStaticPath(const std::string &path)
 {
    if (path.find("..") == std::string::npos) {
         throw (std::runtime_error(
             std::format("Error: {}. Directory traversal detected.", path)));
     }