 
   test ":callback redirects to params[:origin] if auth is ok" do
     Settings.stubs(:authentication).returns(stub(provider: :google_apps))
     @request.env['omniauth.auth'] = { 'info' => { 'email' => 'bob@toto.com' } }
     stack = stacks(:shipit)
 
 
   test ":callback can sign in to github" do
     Settings.stubs(:authentication).returns(stub(provider: :google_apps))
 
     @request.env['omniauth.auth'] = { provider: 'github', info:  { nickname: 'shipit' } }
     github_user = mock('Sawyer User')