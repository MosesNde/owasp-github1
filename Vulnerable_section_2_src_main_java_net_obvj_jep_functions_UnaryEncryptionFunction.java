      */
     public enum EncryptionAlgorithm
     {
        @Function("md5")
        MD5
        {
            @Override
            String execute(String content)
            {
                return EncryptionUtils.md5(content);
            }
        },

         @Function("sha1")
         SHA1
         {