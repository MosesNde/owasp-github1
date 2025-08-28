 static char *filter_item_name(R_NONNULL const char *name) {
 	R_RETURN_VAL_IF_FAIL (name, NULL);
 	char *res = strdup (name);
	if (!res) {
		return NULL;
 	}
	r_str_trim (res);
	r_name_filter (res, 0);
 	return res;
 }
 
 	item->realname = item->name;
 }
 
static bool update_flag_item_addr(RFlag *f, RFlagItem *item, ut64 newaddr, bool is_new, bool force) {
	if (item->addr != newaddr || force) {
 		if (!is_new) {
			remove_addrmap (f, item);
 		}
		item->addr = newaddr;
 		RFlagsAtOffset *flagsAtOffset = flags_at_addr (f, newaddr);
		if (!flagsAtOffset) {
			return false;
 		}
		r_list_append (flagsAtOffset->flags, item);
		R_DIRTY_SET (f);
		return true;
 	}

 	return false;
 }
 
 	return n;
 }
 
R_API void r_flag_item_free(RFlagItem *item) {
	if (R_LIKELY (item)) {
		free (item->color);
		free (item->comment);
		free (item->alias);
 		/* release only one of the two pointers if they are the same */
		free_item_name (item);
		free (item->realname);
		free (item);
 	}
 }
 
 	return false;
 }
 
/* return the flag item with name "name" in the RFlag "f", if it exists.
 * Otherwise, NULL is returned. */
 R_API RFlagItem *r_flag_get(RFlag *f, const char *name) {
 	R_RETURN_VAL_IF_FAIL (f, NULL);
 	RFlagItem *r = ht_pp_find (f->ht_name, name, NULL);
 	return list? evalFlag (f, r_list_last (list)): NULL;
 }
 
/* return the first flag that matches an addr ordered by the order of
 * operands to the function.
 * Pass in the name of each space, in order, followed by a NULL */
 R_API RFlagItem *r_flag_get_by_spaces(RFlag *f, bool prionospace, ut64 addr, ...) {
 	R_RETURN_VAL_IF_FAIL (f, NULL);
 	if (f->mask) {
 
 	const RList *list = r_flag_get_list (f, addr);
 	RFlagItem *ret = NULL;
	const char *spacename;
	RSpace **spaces;
 	RListIter *iter;
	RFlagItem *flg;
 	va_list ap, aq;
	size_t n_spaces = 0, i;
 
 	va_start (ap, addr);
 	// some quick checks for common cases
 
 	// count spaces in the vaarg
 	va_copy (aq, ap);
	spacename = va_arg (aq, const char *);
 	while (spacename) {
 		n_spaces++;
 		spacename = va_arg (aq, const char *);
 	}
 	va_end (aq);
 
 	// get RSpaces from the names
	i = 0;
	spaces = R_NEWS (RSpace *, n_spaces + 1);
 	spacename = va_arg (ap, const char *);
 	while (spacename) {
 		RSpace *space = r_flag_space_get (f, spacename);
 	n_spaces = i;
 
 	ut64 min_space_i = n_spaces + 1;
	r_list_foreach (list, iter, flg) {
 		// get the "priority" of the flag flagspace and
 		// check if better than what we found so far
		if (prionospace && !flg->space) {
			ret = flg;
 			break;
 		}
 		for (i = 0; i < n_spaces; i++) {
			if (flg->space == spaces[i]) {
 				break;
 			}
 			if (i >= min_space_i) {
 
 		if (i < min_space_i) {
 			min_space_i = i;
			ret = flg;
 		}
 		if (!min_space_i) {
 			// this is the best flag we can find, let's stop immediately