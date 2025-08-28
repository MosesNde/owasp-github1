 import freemarker.log.Logger;
 import freemarker.template.utility.SecurityUtilities;
 import freemarker.template.utility.UndeclaredThrowableException;
 
 /**
  * @author Attila Szegedi
 class DebuggerServer
 {
     private static final Logger logger = Logger.getLogger("freemarker.debug.server");
    // TODO: Eventually replace with Yarrow    
    private static final Random R = new SecureRandom();
     
     private final byte[] password;
     private final int port;