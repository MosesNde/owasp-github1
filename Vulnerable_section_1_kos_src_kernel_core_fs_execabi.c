 /* Finalize the given set of exec() arguments. */
 PUBLIC NOBLOCK NONNULL((1)) void
 NOTHROW(FCALL execargs_fini)(struct execargs *__restrict self) {
	if unlikely(self->ea_argc_inject) {
 		size_t i;
 		for (i = 0; i < self->ea_argc_inject; ++i)
 			kfree(self->ea_argv_inject[i]);