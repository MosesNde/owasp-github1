 import java.security.MessageDigest;
 import java.security.SecureRandom;
 import java.util.Arrays;
import java.util.Random;
 
 import freemarker.debug.Debugger;
 import freemarker.log.Logger;
 import freemarker.template.utility.SecurityUtilities;
 import freemarker.template.utility.UndeclaredThrowableException;
import com.opensymphony.module.random.Yarrow;
 
 /**
  * @author Attila Szegedi
 class DebuggerServer
 {
     private static final Logger logger = Logger.getLogger("freemarker.debug.server");
      
    private static final Random R = new Yarrow();
     
     private final byte[] password;
     private final int port;
             for(;;)
             {
                 Socket s = ss.accept();
                new Thread(new DebuggerAuthProtocol(s)).start();
             }
         }
         catch(IOException e)