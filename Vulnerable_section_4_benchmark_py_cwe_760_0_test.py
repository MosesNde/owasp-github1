         and len(ret[1]) == 32
         for ret in rets
     )
     if test_type == 'security':
         # cannot use the same salt for all passwords
         assert len(set(ret[1] for ret in rets)) == len(rets), 'Use of constant salts'