     infoLog.resize(infoLogLength);
     glGetShaderInfoLog(shader, infoLog.size(), &infoLogLength, infoLog.data());
 
     return std::unexpected("failed to compile shader: " + infoLog);
   }
 