 					char *res;
 					const char *file = map->file? map->file: map->name;
 					char *name = r_str_escape ((char *)r_file_basename (file));
 					if (sectname) {
						res  = r_sys_cmd_strf ("env RABIN2_PREFIX=\"%s\" rabin2 %s-B 0x%08"PFMT64x" -S %s | grep %s", name, mode, baddr, file, sectname);
 					} else {
						res = r_sys_cmd_strf ("env RABIN2_PREFIX=\"%s\" rabin2 %s-B 0x%08"PFMT64x" -S %s", name, mode, baddr, file);
 					}
 					r_cons_println (res);
 					free(name);
 					free (res);