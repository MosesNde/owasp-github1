 }
 
 R_API const char *r_name_filter_ro(const char *a) {
	R_RETURN_VAL_IF_FAIL (s, NULL);
	while (*a == '_') {
		a++;
	}
 	return a - 1;
 }
 
 // filter string for printing purposes
 R_API bool r_name_filter_print(char *s) {
 	R_RETURN_VAL_IF_FAIL (s, NULL);
 	char *es = s + strlen (s);
	char *os = s;
 	bool valid = true;
 	while (*s && s < es) {
 		int us = r_utf8_size ((const ut8*)s);