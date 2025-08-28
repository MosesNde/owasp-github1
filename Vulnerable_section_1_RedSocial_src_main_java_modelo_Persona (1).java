 import static org.apache.commons.codec.binary.Base64.decodeBase64;
 import static org.apache.commons.codec.binary.Base64.encodeBase64;
 
 public class Persona {
 	private String nombre, apellidos, username, email, password, direccion, telefono, foto, original, rol;
 	
     }
 	
 	public void encrypt() throws Exception {
        Cipher cipher = Cipher.getInstance(cI);
         SecretKeySpec skeySpec = new SecretKeySpec(key.getBytes(), alg);
         IvParameterSpec ivParameterSpec = new IvParameterSpec(iv.getBytes());
         cipher.init(Cipher.ENCRYPT_MODE, skeySpec, ivParameterSpec);
         byte[] encrypted = cipher.doFinal(getPassword().getBytes());
        setPassword(new String(encodeBase64(encrypted)));
	}
 	
 	public void decrypt() throws Exception {
         Cipher cipher = Cipher.getInstance(cI);