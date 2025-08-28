 	bool show_emu_ssa;
 	bool show_section;
 	int show_section_col;
 	bool show_section_perm;
 	bool show_section_name;
 	bool show_symbols;
 	ds->show_varsum = r_config_get_i (core->config, "asm.var.summary");
 	ds->show_varaccess = r_config_get_i (core->config, "asm.var.access");
 	ds->maxrefs = r_config_get_i (core->config, "asm.xrefs.max");
	ds->maxflags = r_config_get_i (core->config, "asm.maxflags");
 	ds->asm_types = r_config_get_i (core->config, "asm.types");
 	ds->foldxrefs = r_config_get_i (core->config, "asm.xrefs.fold");
 	ds->show_lines = r_config_get_i (core->config, "asm.lines");
 	return strcmp (fa->name, fb->name);
 }
 
 static void ds_show_flags(RDisasmState *ds) {
 	//const char *beginch;
 	RFlagItem *flag;
 	const RList *flaglist = r_flag_get_list (core->flags, ds->at);
 	RList *uniqlist = flaglist? r_list_uniq (flaglist, flagCmp): NULL;
 	int count = 0;
 	r_list_foreach (uniqlist, iter, flag) {
 		if (f && f->addr == flag->offset && !strcmp (flag->name, f->name)) {
 			// do not show flags that have the same name as the function
 			continue;
 		}
 		bool no_fcn_lines = (f && f->addr == flag->offset);
 		if (ds->maxflags && count >= ds->maxflags) {
			ds_pre_xrefs (ds, no_fcn_lines);
			r_cons_printf ("...\n");
 			break;
 		}
 		count++;
 				continue;
 			}
 		}
 			ds_begin_line (ds);
 
 		bool fake_flag_marks = (!ds->show_offset && ds->show_marks);
		if (ds->show_flgoff) {
			ds_pre_line (ds);
			ds_print_offset (ds);
			if (!fake_flag_marks) {
				r_cons_printf (" ");
 			}
		} else {
			ds_pre_xrefs (ds, no_fcn_lines);
 		}
 
 		if (ds->show_color) {
 		}
 
 		if (!ds->show_flgoff || fake_flag_marks) {
			r_cons_printf (";-- ");
 		}
 
 		if (ds->asm_demangle && flag->realname) {
 				}
 				if (name) {
 					r_str_ansi_filter (name, NULL, NULL, -1);
					r_cons_printf ("%s:", name);
 					R_FREE (name);
 				}
 			}
 		} else {
			r_cons_printf ("%s:", flag->name);
 		}
 		if (ds->show_color) {
 			r_cons_strcat (Color_RESET);
 		}
 		ds_newline (ds);
 	}
 	r_list_free (uniqlist);
 	return NULL;
 }
 
 static char *ds_sub_jumps(RDisasmState *ds, char *str) {
 	RAnal *anal = ds->core->anal;
 	RFlag *f = ds->core->flags;
 		return str;
 	}
 	int optype = ds->analop.type & 0xFFFF;
	if (optype < R_ANAL_OP_TYPE_JMP || optype >= R_ANAL_OP_TYPE_RET) {
 		return str;
 	}
 	ut64 addr = ds->analop.jump;