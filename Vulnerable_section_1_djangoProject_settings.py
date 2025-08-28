 def get_login_redirect(request):
     if hasattr(request, 'user') and request.user.is_superuser:
         return '/admin/'
    return LOGIN_REDIRECT_URL
\ No newline at end of file
\ No newline at end of file