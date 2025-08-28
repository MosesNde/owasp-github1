 import java.util.Optional;
 
 public interface UserRepository extends JpaRepository<User, Long> {
     boolean existsByEmail(String email);
     boolean existsByPhoneNumber(String phoneNumber);
    Optional<User> findByUsernameAndPassword(String username, String password);
    Optional<User> findByUsername(String username);
 }