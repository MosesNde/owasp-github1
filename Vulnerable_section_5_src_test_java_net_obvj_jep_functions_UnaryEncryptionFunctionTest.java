  */
 public class UnaryEncryptionFunctionTest
 {
    private static UnaryEncryptionFunction md5 = new UnaryEncryptionFunction(EncryptionAlgorithm.MD5);
     private static UnaryEncryptionFunction sha1 = new UnaryEncryptionFunction(EncryptionAlgorithm.SHA1);
     private static UnaryEncryptionFunction sha256 = new UnaryEncryptionFunction(EncryptionAlgorithm.SHA256);
     private static UnaryEncryptionFunction toBase64 = new UnaryEncryptionFunction(EncryptionAlgorithm.TO_BASE64);
     private static UnaryEncryptionFunction fromBase64 = new UnaryEncryptionFunction(EncryptionAlgorithm.FROM_BASE64);
 
    /**
     * Tests the MD5 function with a valid string
     */
    @Test
    public void testMd5WithValidString() throws ParseException
    {
        Stack<Object> parameters = CollectionsUtils.newParametersStack("asd");
        md5.run(parameters);
        assertEquals("7815696ecbf1c96e6894b779456d330e", parameters.pop());
    }

     /**
      * Tests the SHA1 function with a valid string
      */