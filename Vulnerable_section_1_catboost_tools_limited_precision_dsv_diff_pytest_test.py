 
 def make_data_file(contents):
     filename = yatest.common.output_path(hex(hash(contents))[-8:])
    open(filename, 'wt').write(contents)
     return filename
 
 
     cmd = (PROGRAM_BINARY_PATH,) + args
     stdout_file = yatest.common.test_output_path('stdout')
     with pytest.raises(yatest.common.ExecutionError):
        yatest.common.execute(cmd, stdout=open(stdout_file, 'w'))
 
     return [local_canonical_file(stdout_file)]
 