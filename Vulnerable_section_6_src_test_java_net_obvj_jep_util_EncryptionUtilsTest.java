         assertThat(EncryptionUtils.class, instantiationNotAllowed());
     }
 
    /**
     * Tests the successful encryption of a string message with MD5
     */
    @Test
    public void testMd5()
    {
        assertThat(EncryptionUtils.md5("asd"), is("7815696ecbf1c96e6894b779456d330e"));
    }

     /**
      * Tests the successful encryption of a string message with SHA1
      */