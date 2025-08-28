 				args->ea_argv_inject[0] = inject_arg0;
 				if (inject_arg1)
 					args->ea_argv_inject[1] = inject_arg1;
 			} EXCEPT {
 				decref_unlikely(interp_path);
 				decref_unlikely(interp_dentry);