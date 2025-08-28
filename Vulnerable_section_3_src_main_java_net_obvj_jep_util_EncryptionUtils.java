         }
     }
 
    /**
     * Computes the MD5 hash for the given string and transforms the binary result into a
     * hexadecimal lower case string.
     *
     * @param content a string input to encrypt
     * @return the MD5 hash transformed into a hexadecimal lower case string.
     */
    public static String md5(String content)
    {
        return hashWith("MD5", content);
    }

     /**
      * Computes the SHA1 hash for the given string and transforms the binary result into a
      * hexadecimal lower case string.