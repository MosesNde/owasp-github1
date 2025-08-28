         }
         else if (jsCryptoAlgo.equals("AES-128-CBC")) {
             // 128 bits -> 16 bytes
            return new CryptoAlgoKeySize("AES", 16);
         }
         else if (jsCryptoAlgo.equals("AES-192-CBC")) {
             // 128 bits -> 16 bytes
            return new CryptoAlgoKeySize("AES", 24);
         }
         else if (jsCryptoAlgo.equals("AES-256-CBC")) {
             // 128 bits -> 16 bytes
            return new CryptoAlgoKeySize("AES", 32);
         }
         else if (jsCryptoAlgo.equals("SHA256")) {
             return new CryptoAlgoKeySize("HmacSHA256");