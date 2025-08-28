  * @return     std::vector<std::string>
  */
 std::vector<std::string> Employees::Select::selectAll(const Employees::EmployeeInfo &info) {
  *result = db->execute("SELECT * FROM Employees WHERE " + info.arg + " = '" + info.data + "'");
   return (result->empty()) ? std::vector<std::string>{} : (*result)[0]; // Return the first and the only row
 }
 
  * @return        std::vector<std::string>
  */
 std::vector<std::string> Employees::Select::selectAll(const Employees::EmployeeInfo &info_00, const Employees::EmployeeInfo &info_01) {
  *result = db->execute("SELECT * FROM Employees WHERE " + info_00.arg + " = '" + info_00.data + "' AND " + info_01.arg + " = '" + info_01.data + "'");
   return (result->empty()) ? std::vector<std::string>{} : (*result)[0]; // Return the first and the only row
 }
 
  */
 int Employees::Update::update(const Employees::EmployeeInfo &info_00, const Employees::EmployeeInfo &info_01) {
   int aff;
  return db->execute("UPDATE Employees SET " + info_00.arg + " = '" + info_00.data + "' WHERE " + info_01.arg + " = '" + info_01.data + "'", aff), aff;
 }
\ No newline at end of file