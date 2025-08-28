/* radare - LGPL - Copyright 2011-2019 - pancake */
 
 #include <r_core.h>
 
 		if (q) {
 			*q = 0;
 		}
		r_core_cmdf (core, "s %s", str);
		r_core_cmdf (core, "\"w %s\"", p+1);
 		break;
 	case ':':
		r_core_cmdf (core, "s %s", str);
		r_core_cmdf (core, "\"wa %s\"", p);
 		break;
 	case 'v':
		q = strchr (p + 1,' ');
 		if (q) {
 			*q = 0;
			for (q++; *q == ' '; q++) {
				; // XXX: skipsspaces here
			}
 		} else {
 			return 0;
 		}
		r_core_cmdf (core, "s %s", str);
		r_core_cmdf (core, "wv%s %s", p + 1, q);
 		break;
 	default:
		r_core_cmdf (core, "s %s", str);
		r_core_cmdf (core, "wx %s", p);
 		break;
 	}
 	return true;