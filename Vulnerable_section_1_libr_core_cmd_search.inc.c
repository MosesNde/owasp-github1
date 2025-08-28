 	const char *cmdhit = r_config_get (core->config, "cmd.hit");
 	param->count++;
 	if (R_STR_ISNOTEMPTY (cmdhit)) {
		r_core_cmdf (core, "%s @ 0x%"PFMT64x, cmdhit, hit->addr);
 	}
	if (!str)
	switch (param->outmode) {
	case R_MODE_JSON:
		pj_o (param->pj);
		pj_kn (param->pj, "offset", hit->addr);
		pj_ki (param->pj, "len", hit->len);
		pj_ks (param->pj, "code", hit->code);
		pj_end (param->pj);
		break;
	case R_MODE_RADARE:
		r_cons_printf ("f %s%d_%i = 0x%08"PFMT64x "\n",
				param->searchprefix, kwidx, param->count, hit->addr);
		break;
	default:
		if (asm_sub_names) {
			char tmp[128] = { 0 };
			RAnalHint *hint = r_anal_hint_get (core->anal, hit->addr);
			const bool be = R_ARCH_CONFIG_IS_BIG_ENDIAN (core->rasm->config);
			r_parse_filter (core->parser, hit->addr, core->flags, hint, hit->code, tmp, sizeof (tmp), be);
			r_anal_hint_free (hint);
			if (param->outmode == R_MODE_SIMPLE) {
				r_cons_printf ("0x%08"PFMT64x "   # %i: %s\n", hit->addr, hit->len, tmp);
			} else {
				char *s = (hit->len > 0)
					? r_core_cmd_strf (core, "pDi %d @e:asm.flags=0@0x%08"PFMT64x, (int)hit->len, hit->addr)
					: r_core_cmd_strf (core, "pdi 1 @e:asm.flags=0@0x%08"PFMT64x, hit->addr);
				if (s) {
					r_cons_printf ("%s", s);
 				}
				free (s);
 			}
		} else {
			r_cons_printf ("0x%08"PFMT64x "   # %i: %s\n", hit->addr, hit->len, r_str_get (hit->code));
 		}
		break;
 	}
 	if (param->searchflags) {
 		if (R_STR_ISNOTEMPTY (str)) {
 	return NULL;
 }
 
 static bool do_analstr_search(RCore *core, struct search_parameters *param, bool quiet, const char *input) {
 	const bool badpages = r_config_get_b (core->config, "search.badpages");
 	bool silent = false;
 						}
 						if (R_STR_ISNOTEMPTY (s)) {
 							char *ss = r_str_trim_dup (s);
							if (json) {
								pj_o (pj);
								pj_kn (pj, "addr", firstch);
								pj_ks (pj, "text", ss);
								pj_end (pj);
							} else {
								r_strbuf_appendf (rb, "0x%08"PFMT64x" %s\n", firstch, ss);
								r_name_filter (ss, -1);
								RCoreAsmHit cah = {
									.addr = firstch,
									.len = lastch - firstch,
								};
								search_hit_at (core, param, &cah, ss);
 							}
 							free (ss);
 						}