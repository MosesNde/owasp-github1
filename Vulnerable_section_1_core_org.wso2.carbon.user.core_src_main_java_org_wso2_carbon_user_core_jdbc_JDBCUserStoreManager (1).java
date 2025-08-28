 import java.util.LinkedList;
 import java.util.List;
 import java.util.Map;
import java.util.Random;
 
 public class JDBCUserStoreManager extends AbstractUserStoreManager {
 
     private static final String SQL_FILTER_STRING_ANY = "%";
     private static final char SQL_FILTER_CHAR_ESCAPE = '\\';
     private static final String CASE_INSENSITIVE_USERNAME = "CaseInsensitiveUsername";
 
     protected DataSource jdbcds = null;
    protected Random random = new Random();
 
     public JDBCUserStoreManager() {
 
 
             if ("true".equalsIgnoreCase(realmConfig.getUserStoreProperties()
                     .get(JDBCRealmConstants.STORE_SALTED_PASSWORDS))) {
                byte[] bytes = new byte[16];
                random.nextBytes(bytes);
                saltValue = Base64.encode(bytes);
             }
 
             password = this.preparePassword(password, saltValue);
         String saltValue = null;
         if ("true".equalsIgnoreCase(realmConfig.getUserStoreProperties().get(
                 JDBCRealmConstants.STORE_SALTED_PASSWORDS))) {
            byte[] bytes = new byte[16];
            random.nextBytes(bytes);
            saltValue = Base64.encode(bytes);
         }
 
         String password = this.preparePassword((String) newCredential, saltValue);
         return date;
     }
 
     /**
      * @param dbConnection
      * @param sqlStmt