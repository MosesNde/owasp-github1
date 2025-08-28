 	for (i = 0; says[i]; i++) {
 		char *sayPath = r_file_path (says[i]);
 		if (sayPath) {
			char *line = r_str_replace (strdup (txt), "\"", "'", 1);
			r_sys_cmdf ("\"%s\" \"%s\"%s", sayPath, line, bg? " &": "");
 			free (line);
 			free (sayPath);
 			return true;