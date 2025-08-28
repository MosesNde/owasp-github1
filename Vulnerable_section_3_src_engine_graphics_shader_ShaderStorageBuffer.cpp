 
   const GLenum error = glGetError();
   if (error != GL_NO_ERROR) {
     return std::unexpected(std::format("glNamedBufferData failed: 0x{:04x}", error));
   }
 