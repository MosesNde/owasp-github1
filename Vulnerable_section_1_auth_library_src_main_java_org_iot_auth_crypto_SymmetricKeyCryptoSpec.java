         }
         else if (jsCryptoAlgo.equals("AES-128-CBC")) {
             // 128 bits -> 16 bytes
            return new CryptoAlgoKeySize("AES/CBC/PKCS5Padding", 16);
         }
         else if (jsCryptoAlgo.equals("AES-192-CBC")) {
             // 128 bits -> 16 bytes
            return new CryptoAlgoKeySize("AES/CBC/PKCS5Padding", 24);
         }
         else if (jsCryptoAlgo.equals("AES-256-CBC")) {
             // 128 bits -> 16 bytes
            return new CryptoAlgoKeySize("AES/CBC/PKCS5Padding", 32);
         }
         else if (jsCryptoAlgo.equals("SHA256")) {
             return new CryptoAlgoKeySize("HmacSHA256");