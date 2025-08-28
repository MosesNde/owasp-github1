     glAttachShader(program, **shader);
     const GLenum error = glGetError();
     if (error != GL_NO_ERROR) {
       return std::unexpected(std::format("glAttachShader error: 0x{:04x}", error));
     }
   }
     infoLog.resize(infoLogLength);
     glGetProgramInfoLog(program, infoLog.size(), &infoLogLength, infoLog.data());
 
     return std::unexpected("failed to link program: " + infoLog);
   }
 