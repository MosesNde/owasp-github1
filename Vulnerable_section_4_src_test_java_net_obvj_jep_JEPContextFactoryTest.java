 
     private void checkCryptoFunctions(FunctionTable table)
     {
        checkFunction(table, "md5", UnaryEncryptionFunction.class, EncryptionAlgorithm.MD5);
         checkFunction(table, "sha1", UnaryEncryptionFunction.class, EncryptionAlgorithm.SHA1);
         checkFunction(table, "sha256", UnaryEncryptionFunction.class, EncryptionAlgorithm.SHA256);
         checkFunction(table, "toBase64", UnaryEncryptionFunction.class, EncryptionAlgorithm.TO_BASE64);