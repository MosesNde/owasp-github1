 				if (idx == skip) {
 					free (dis);
 					curat = refi->addr;
					char *res = r_core_cmd_strf (core, "pd 4 @ 0x%08"PFMT64x"@e:asm.maxflags=1", refi->at);
 					// TODO: show disasm with context. not seek addr
 					// dis = r_core_cmd_strf (core, "pd $r-4 @ 0x%08"PFMT64x, refi->addr);
 					dis = NULL;