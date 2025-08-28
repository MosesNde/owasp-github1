 						}
 					}
 					*ptr = 0;
					snprintf (str, len, "%s%s%s", data, f->realnames? flag->realname : flag->name,
							(ptr != ptr2) ? ptr2 : "");
 					bool banned = false;
 					{
 						const char *p = strchr (str, '[');