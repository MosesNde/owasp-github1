 				ut64 addr = core->addr;
 				RAnalFunction *fcn = r_anal_get_fcn_in (core->anal, addr, -1);
 				if (fcn) {
					r_cons_printf ("f %s=0x%08"PFMT64x"\n", fcn->name, addr);
					r_cons_printf ("afn %s @ 0x%08"PFMT64x"\n", fcn->name, addr);
 					char *sig = r_core_cmd_str (core, "afs");
 					r_str_trim (sig);
 					r_str_replace_char (sig, ',', 0);
					r_cons_printf ("afs %s @ 0x%08"PFMT64x"\n", sig, addr);
 					free (sig);
 				}
 				}
 				if (fcn) {
 					char *name = r_core_anal_fcn_autoname (core, fcn, 'v');
 					if (name) {
						r_cons_printf ("afn %s 0x%08" PFMT64x "\n", name, core->addr);
 						free (name);
 					}
 				} else {