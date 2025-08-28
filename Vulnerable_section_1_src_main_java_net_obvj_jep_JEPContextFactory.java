         registerFunction(NamedPackage.UTIL, () -> new UnarySystemFunction(UnarySystemFunction.Strategy.GET_SYSTEM_PROPERTY));
 
         // Cryptography functions
        registerFunction(NamedPackage.CRYPTO, () -> new UnaryEncryptionFunction(EncryptionAlgorithm.MD5));
         registerFunction(NamedPackage.CRYPTO, () -> new UnaryEncryptionFunction(EncryptionAlgorithm.SHA1));
         registerFunction(NamedPackage.CRYPTO, () -> new UnaryEncryptionFunction(EncryptionAlgorithm.SHA256));
         registerFunction(NamedPackage.CRYPTO, () -> new UnaryEncryptionFunction(EncryptionAlgorithm.TO_BASE64));