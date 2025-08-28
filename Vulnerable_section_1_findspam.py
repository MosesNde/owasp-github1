          'reason': "pattern-matching website in {}", 'title': True, 'body': True, 'username': True,
          'stripcodeblocks': False, 'body_summary': True, 'max_rep': 4, 'max_score': 2},
         # Links preceded by arrows >>>
        {'regex': r"(?is)(?:>>>+|@+>>+|@@+>+|==\s*>>+|={4,}|===>+|= = =|(Read More|Click Here)).{0,20}"
                   r"https?://(?!i\.stack\.imgur\.com)(?=.{,200}$)", 'all': True,
          'sites': [], 'reason': "link following arrow in {}", 'title': True, 'body': True, 'username': True,
          'stripcodeblocks': True, 'body_summary': False, 'answers': False, 'max_rep': 11, 'max_score': 0},