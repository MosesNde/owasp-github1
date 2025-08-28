                 vm->insts[pc++] = (struct ebpf_inst) {.opcode = EBPF_OP_JSGE_IMM, .dst = 11, .src = 0, .offset = 1, .imm = 0};
                 /* We failed the test, jump to the error */
                 vm->insts[pc++] = (struct ebpf_inst) {.opcode = EBPF_OP_JA, .dst = 0, .src = 0, .offset = 1, .imm = 0};
                /* Step 2: check that the accessed pointer - memory_size < memory_ptr */
                vm->insts[pc++] = (struct ebpf_inst) {.opcode = EBPF_OP_JLT_IMM, .dst = 11, .src = 0, .offset = 13, .imm = memory_size};
                 /* We failed one of the tests for the store, but maybe we try to access the stack from another register than R10? */
                 /* Step 3: check that the accessed pointer is <= stack_ptr */
                 vm->insts[pc++] = (struct ebpf_inst) {.opcode = EBPF_OP_MOV64_REG, .dst = 11, .src = inst.src, .offset = 0, .imm = 0};
                 vm->insts[pc++] = (struct ebpf_inst) {.opcode = EBPF_OP_JSGE_IMM, .dst = 11, .src = 0, .offset = 1, .imm = 0};
                 /* We failed the test, jump to the error */
                 vm->insts[pc++] = (struct ebpf_inst) {.opcode = EBPF_OP_JA, .dst = 0, .src = 0, .offset = 1, .imm = 0};
                /* Step 2: check that the accessed pointer - memory_size < memory_ptr */
                vm->insts[pc++] = (struct ebpf_inst) {.opcode = EBPF_OP_JLT_IMM, .dst = 11, .src = 0, .offset = 13, .imm = memory_size};
                 /* We failed one of the tests for the store, but maybe we try to access the stack from another register than R10? */
                 /* Step 3: check that the accessed pointer is <= stack_ptr */
                 vm->insts[pc++] = (struct ebpf_inst) {.opcode = EBPF_OP_MOV64_REG, .dst = 11, .src = inst.dst, .offset = 0, .imm = 0};