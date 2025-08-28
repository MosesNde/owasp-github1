         }
     }
 
    // Java program to calculate MD5 hash value
    public static String md5(String input)
     {
         try {
 
            // Static getInstance method is called with hashing MD5
            MessageDigest md = MessageDigest.getInstance("MD5");
 
             // digest() method is called to calculate message digest
             //  of an input digest() return array of byte
             byte[] messageDigest = md.digest(input.getBytes());
 
             // Convert byte array into signum representation