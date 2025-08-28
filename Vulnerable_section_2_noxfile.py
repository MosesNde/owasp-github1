         'python',
         '-m',
         'pytest',
         '--basetemp',
         './log',
        '--junitxml=junit.xml',
        '--html=report.html',
     ]
    timeout = 60
     if config.get('exitfirst', True):
         ret.append('--exitfirst')
     if config.get('verbose', True):
         ret.append('--verbose')
     if config.get('fail_on_warnings'):
         ret.insert(1, 'error')
         ret.insert(1, '-W')
    if config.get('timeout'):
        timeout = config["timeout"]
    ret.append(f'--timeout={timeout}')
     if config.get('pdb'):
         ret.append('--pdb')
    if config.get('coverage'):
        ret.append('--cov-report=html')
        ret.append('--cov=pyroute2')
     if config.get('tests_prefix'):
         module = f'{config["tests_prefix"]}/{module}'
     if config.get('sub'):