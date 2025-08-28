 			r_flag_zone_reset (f);
 		}
 		zi = R_NEW0 (RFlagZoneItem);
		if (R_LIKELY (zi)) {
			zi->name = strdup (name);
			zi->from = zi->to = addr;
			r_list_append (f->zones, zi);
		} else {
			return false;
		}
 	}
 	return true;
 }
 	RList *db = f->zones;
 	r_list_foreach (db, iter, zi) {
 		if (mode == '*') {
			f->cb_printf ("fz %s @ 0x08%"PFMT64x"\n", zi->name, zi->from);
			f->cb_printf ("f %s %"PFMT64d" 0x08%"PFMT64x"\n", zi->name,
 				zi->to - zi->from, zi->from);
 		} else if (mode == 'q') {
 			f->cb_printf ("%s\n", zi->name);