 			} else {
 				name = r_str_newf ("entry%i", i);
 			}
			r_cons_printf ("f %s 1 @ 0x%08"PFMT64x"\n", name, at);
			r_cons_printf ("f %s_%s 1 @ 0x%08"PFMT64x"\n", name, hpaddr_key, hpaddr);
			r_cons_printf ("s %s\n", name);
 			free (name);
 		} else {
 			r_cons_printf ("vaddr=0x%08"PFMT64x" paddr=0x%08"PFMT64x, at, paddr);
 		}
 		if (bin_demangle) {
 			demname = r_bin_demangle (r->bin->cur, lang, str, addr);
 		}
 		r_name_filter (str, 0);
 		fi = r_flag_set (r->flags, str, addr, bin_reloc_size (reloc));
 	RBinFile * binfile = r->bin->cur;
 	RBinObject *binobj = binfile ? binfile->o: NULL;
 	RBinInfo *info = binobj ? binobj->info: NULL;
	int cdsz;
 
	cdsz = info? (info->bits == 64? 8: info->bits == 32? 4: info->bits == 16 ? 4: 0): 0;
 	if (cdsz == 0) {
 		return;
 	}
 	if (IS_MODE_SET (mode)) {
 		r_meta_add (r->anal, R_META_TYPE_DATA, reloc->vaddr, reloc->vaddr + cdsz, NULL);
 	} else if (IS_MODE_RAD (mode)) {
		r_cons_printf ("f Cd %d @ 0x%08" PFMT64x "\n", cdsz, addr);
 	}
 }
 
 				}
 			}
 			if (name) {
				r_cons_printf ("f %s%s%s @ 0x%08"PFMT64x"\n",
 					r->bin->prefix ? r->bin->prefix : "reloc.",
					r->bin->prefix ? "." : "", name, addr);
 				add_metadata (r, reloc, addr, mode);
 				free (name);
 			}