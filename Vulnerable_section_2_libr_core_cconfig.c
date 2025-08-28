 	return true;
 }
 
 static int cb_midflags (void *user, void *data) {
 	RConfigNode *node = (RConfigNode *)data;
 	if (node->value[0] == '?') {
 	SETPREF ("asm.strip", "", "strip all instructions given comma separated types");
 	SETPREF ("asm.lines.fcn", "true", "Show function boundary lines");
 	SETPREF ("asm.flags", "true", "Show flags");
 	SETPREF ("asm.flags.offset", "false", "Show offset in flags");
 	SETPREF ("asm.flags.inbytes", "false",  "Display flags inside the bytes space");
 	n = NODEICB ("asm.flags.middle", 2, &cb_midflags);
 	SETOPTIONS (n, "0 = do not show flag", "1 = show without realign", "2 = realign at middle flag",
 		"3 = realign at middle flag if sym.*", NULL);
 	SETPREF ("asm.lines.wide", "false", "Put a space between lines");
 	SETPREF ("asm.fcnsig", "true", "Show function signature in disasm");
 	SETICB ("asm.lines.width", 7, &cb_asmlineswidth, "Number of columns for program flow arrows");
	SETI ("asm.maxflags", 0, "Maximum number of flags to show in a single offset");
 	SETICB ("asm.var.submin", 0x100, &cb_asmvarsubmin, "Minimum value to substitute in instructions (asm.var.sub)");
 	SETCB ("asm.tailsub", "false", &cb_asmtailsub, "Replace addresses with prefix .. syntax");
 	SETPREF ("asm.middle", "false", "Allow disassembling jumps in the middle of an instruction");