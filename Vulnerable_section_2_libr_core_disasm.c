 				&& (arch = r_config_get (ds->core->config, "asm.arch"))
 				&& strcmp (arch, "dalvik")) {
 			RFlagItem *flag_sym = flag;
			if (ds->core->vmode && ds->asm_demangle
 					&& (r_str_startswith (flag->name, "sym.")
 						|| (flag_sym = r_flag_get_by_spaces (ds->core->flags, false,
							ds->analop.jump, R_FLAGS_FS_SYMBOLS, NULL)))
				&& flag_sym->demangled) {
 				return;
 			}
 			ds_begin_comment (ds);