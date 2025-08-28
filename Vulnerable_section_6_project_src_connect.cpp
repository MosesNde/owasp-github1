 
 // ? Function/Class prototype dev part
 
 // * ===========================================
 // ? === Database Constructor and destructor ===
 // * ===========================================
 
  *
  * @class              Database
  * @param query        {const std::string &}
  * @param affectedRows {int &} -> Default:0
  */
void Database::execute(const std::string &query, int &affectedRows) {
   affectedRows = 0; // Default to 0 affected rows
 
   try {
     Statement *stmt = conn->createStatement(query);
     affectedRows = stmt->executeUpdate(); // For INSERT, UPDATE, DELETE queries
     conn->terminateStatement(stmt);
   } catch (SQLException &e) {
     std::cerr << "Query Error: " << e.getMessage() << std::endl;
 /**
  * @brief ### Executes `SELECT` SQL query and return the `results`
  *
 * @class       Database
 * @param query {const std::string &}
 * @return      std::vector<std::vector<std::string>>
  */
std::vector<std::vector<std::string>> Database::execute(const std::string &query) {
   std::vector<std::vector<std::string>> results;
   try {
     Statement *stmt = conn->createStatement(query);
 
     ResultSet *rs = stmt->executeQuery();
    int columnCount = rs->getColumnListMetaData().size();
 
     while (rs->next()) {
       std::vector<std::string> row;
       for (int i = 1; i <= columnCount; ++i)
         row.push_back(rs->getString(i));
       results.push_back(row);
     }
    stmt->closeResultSet(rs);
 
     conn->terminateStatement(stmt);
   } catch (SQLException &e) {
     std::cerr << "Query Error: " << e.getMessage() << std::endl;
   }
 
  return results;
 }
 
 // * ============================