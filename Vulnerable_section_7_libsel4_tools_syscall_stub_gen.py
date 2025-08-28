         Type("seL4_Bool", 1, wordsize, native_size_bits=8),
 
         # seL4 Structures
        BitFieldType("seL4_PrioProps_t", wordsize, wordsize),
         BitFieldType("seL4_CapRights_t", wordsize, wordsize),
 
         # Object types