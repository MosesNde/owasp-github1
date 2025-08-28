 	pair (key, sdb_fmt ("%"PFMT64d, val), mode, last);
 }
 
 static void pair_ut64x(const char *key, ut64 val, int mode, bool last) {
 	const char *str_val = IS_MODE_JSON (mode) ? sdb_fmt ("%"PFMT64d, val) : sdb_fmt ("0x%"PFMT64x, val);
 	pair (key, str_val, mode, last);
 			} else {
 				name = r_str_newf ("entry%i", i);
 			}
			r_cons_printf ("\"f %s 1 0x%08"PFMT64x"\"\n", name, at);
			r_cons_printf ("\"f %s_%s 1 0x%08"PFMT64x"\"\n", name, hpaddr_key, hpaddr);
			r_cons_printf ("\"s %s\"\n", name);
 			free (name);
 		} else {
 			r_cons_printf ("vaddr=0x%08"PFMT64x" paddr=0x%08"PFMT64x, at, paddr);
 			}
 			if (name) {
 				int reloc_size = 4;
 				r_cons_printf ("\"f %s%s%s %d 0x%08"PFMT64x"\"\n",
 					r->bin->prefix ? r->bin->prefix : "reloc.",
					r->bin->prefix ? "." : "", name, reloc_size, addr);
 				add_metadata (r, reloc, addr, mode);
 				free (name);
 			}
 		} else if (IS_MODE_JSON (mode)) {
 
 static char *construct_symbol_flagname(const char *pfx, const char *symname, int len) {
 	char *r = r_str_newf ("%s.%s", pfx, symname);
	if (!r) {
		return NULL;
 	}
	r_name_filter (r, len);
	return r;
 }
 
 typedef struct {
 	}
 	sn->name = strdup (sym->name);
 	const char *pfx = getPrefixFor (sym->type);
	sn->nameflag = construct_symbol_flagname(pfx, r_bin_symbol_name (sym), MAXFLAG_LEN_DEFAULT);
 	if (sym->classname && sym->classname[0]) {
 		sn->classname = strdup (sym->classname);
 		sn->classflag = r_str_newf ("sym.%s.%s", sn->classname, sn->name);
 				lastfs = 'i';
 			} else {
 				if (lastfs != 's') {
					r_cons_printf ("fs %s\n",
						exponly? "exports": "symbols");
 				}
 				lastfs = 's';
 			}
 				r_cons_printf ("\"f %s%s%s %u 0x%08" PFMT64x "\"\n",
 					r->bin->prefix ? r->bin->prefix : "", r->bin->prefix ? "." : "",
 					flagname, symbol->size, addr);
				free(flagname);
 			}
 			binfile = r_bin_cur (r->bin);
 			plugin = r_bin_file_cur_plugin (binfile);
 					char *module = strdup (r_symbol_name);
 					char *p = strstr (module, ".dll_");
 					if (p && strstr (module, "imp.")) {
						const char *symname = p + 5;
 						*p = 0;
 						if (r->bin->prefix) {
 							r_cons_printf ("k bin/pe/%s/%d=%s.%s\n",
 							r_cons_printf ("k bin/pe/%s/%d=%s\n",
 								module, symbol->ordinal, symname);
 						}
 					}
 					free (module);
 				}
 			bits = R_SYS_BITS;
 		}
 		if (IS_MODE_RAD (mode)) {
			r_cons_printf ("f %s.%s = 0x%08"PFMT64x"\n", type, section->name, section->vaddr);
 		} else if (IS_MODE_SET (mode)) {
 #if LOAD_BSS_MALLOC
 			if (!strcmp (section->name, ".bss")) {
 		ut64 addr = rva (bin, field->paddr, field->vaddr, va);
 
 		if (IS_MODE_RAD (mode)) {
			r_name_filter (field->name, -1);
			r_cons_printf ("f header.%s @ 0x%08"PFMT64x"\n", field->name, addr);
 			if (field->comment && *field->comment) {
				r_cons_printf ("CC %s @ 0x%"PFMT64x"\n", field->comment, addr);
				r_cons_printf ("Cf %d .%s @ 0x%"PFMT64x"\n", field->size, field->format, addr);
 			}
 			if (field->format && *field->format) {
				r_cons_printf ("pf.%s %s\n", field->name, field->format);
 			}
 		} else if (IS_MODE_JSON (mode)) {
 			r_cons_printf ("%s{\"name\":\"%s\","
 				"\"vaddr\":%"PFMT64d","
 				c->addr, at_min, at_max, c->name, c->super ? " " : "",
 				c->super ? c->super : "");
 		} else if (IS_MODE_RAD (mode)) {
			r_cons_printf ("\"f class.%s = 0x%"PFMT64x"\"\n",
				name, at_min);
 			if (c->super) {
 				r_cons_printf ("\"f super.%s.%s = %d\"\n",
					c->name, c->super, c->index);
 			}
 			r_list_foreach (c->methods, iter2, sym) {
 				char *mflags = r_core_bin_method_flags_str (sym->method_flags, mode);
				char *cmd = r_str_newf ("\"f method%s.%s.%s = 0x%"PFMT64x"\"\n", mflags, c->name, sym->name, sym->vaddr);
 				if (cmd) {
 					r_str_replace_char (cmd, ' ', '_');
 					if (strlen (cmd) > 2) {
 			// Nothing to set.
 			// TODO: load libraries with iomaps?
 		} else if (IS_MODE_RAD (mode)) {
			r_cons_printf ("CCa entry0 %s\n", lib);
 		} else if (IS_MODE_JSON (mode)) {
 			r_cons_printf ("%s\"%s\"", iter->p ? "," : "", lib);
 		} else {
 
 	switch (mode) {
 	case '*':
		r_cons_printf ("oba 0x%08"PFMT64x" %s # %d\n", bf->o->boffset, name, bf->id);
 		break;
 	case 'q':
 		r_cons_printf ("%d\n", bf->id);