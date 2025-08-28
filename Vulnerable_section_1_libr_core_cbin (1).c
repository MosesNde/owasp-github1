 	r_cons_printf ("public class %s {\n", cn);
 	free (pn);
 	r_list_foreach (c->fields, iter2, f) {
		if (f->name && r_regex_match ("ivar","e", f->name)) {
 			r_cons_printf ("  public %s %s\n", f->type, f->name);
 		}
 	}
 			}
 			r_list_foreach (c->fields, iter2, f) {
 				char *fn = r_str_newf ("field.%s.%s", c->name, f->name);
 				ut64 at = f->vaddr; //  sym->vaddr + (f->vaddr &  0xffff);
 				r_cons_printf ("\"f %s = 0x%08"PFMT64x"\"\n", fn, at);
 				free (fn);