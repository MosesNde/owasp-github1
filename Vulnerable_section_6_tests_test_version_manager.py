 def manager():
     with patch.dict('os.environ', {
         'JIRA_BASE_URL': 'https://jira.example.com',
        'JIRA_API_TOKEN': 'test-token',
        'JIRA_PROJECT_KEYS': 'TEST1,TEST2',
        'JIRA_VERSION_FORMATS': '{}.W{:02d}.{}.{:02d}.{:02d}'
     }):
         return JiraVersionManager()
 
     manager._make_request('GET', 'https://example.com')
     
     args, kwargs = mock_request.call_args
    assert kwargs['verify'] is True 
\ No newline at end of file
\ No newline at end of file