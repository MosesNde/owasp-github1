 		try {
 			String secretMessage = "Some Message to Encrypt";
 
			Cipher encryptCipher = Cipher.getInstance("RSA");
 
 			String publicKeyString = getFile("/public.key");
 
 
 		try {
 
			Cipher decryptCipher = Cipher.getInstance("RSA");
 
 			String privateKeyString = getFile("/private_key.pem");
 