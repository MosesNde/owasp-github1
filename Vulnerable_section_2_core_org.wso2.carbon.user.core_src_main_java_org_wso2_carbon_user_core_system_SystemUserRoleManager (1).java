 import java.util.Date;
 import java.util.LinkedList;
 import java.util.List;
import java.util.Random;
 
 public class SystemUserRoleManager {
 
     private static Log log = LogFactory.getLog(SystemUserRoleManager.class);
     int tenantId;
     private DataSource dataSource;
    private Random random = new Random();
 
     public SystemUserRoleManager(DataSource dataSource, int tenantId) throws UserStoreException {
         super();
             String sqlStmt1 = SystemJDBCConstants.ADD_USER_SQL;
 
             String saltValue = null;
            byte[] bytes = new byte[16];
            random.nextBytes(bytes);
            saltValue = Base64.encode(bytes);
 
             password = this.preparePassword(password, saltValue);
 