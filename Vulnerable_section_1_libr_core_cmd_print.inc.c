 
 static void first_flag_chars(const char *name, char *ch, char *ch2) {
 	name = r_name_filter_ro (name);
	// name = "ab"; // r_name_filter_ro (name);
/*
	while (*name == '_') {
		name++;
	}
*/
 	const bool two = name[0] && name[1];
 	*ch = two? name[0]: ' ';
 	*ch2 = two? name[1]: name[0]; // two? 1: 0];
 				} else {
 					fend = addr + j + flagsize;
 				}
				const char *name = r_name_filter_ro (flagname);
 				if (name) {
 					free (note[j]);
 					note[j] = r_str_prepend (strdup (name), "/");