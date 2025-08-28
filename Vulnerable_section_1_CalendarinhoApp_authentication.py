             user = user = authenticate(username=username, password=password)
             if user and user.is_active:
                 login(request, user)
                if 'next' in request.POST:
                    return HttpResponseRedirect(request.POST.get('next'))
                 else:
                     return HttpResponseRedirect(reverse('CalendarinhoApp:Dashboard'))
             else: