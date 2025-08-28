 from django.http import HttpResponse, HttpResponseBadRequest
 from django.shortcuts import redirect, render
 from django.urls import reverse
 from django.utils.translation import gettext as _
 from django.views.decorators.debug import sensitive_post_parameters
 from django.views.decorators.http import require_POST
 
             # redirect to this view again so the staff mode middleware runs for the authenticated user.
             redirect_to = request.GET.get("next", None)
            if redirect_to:
                return redirect(reverse("evaluation:index") + "?next=" + redirect_to)

            return redirect("evaluation:index")
 
     # if not logged in by now, render form
     if not request.user.is_authenticated:
 
     # check for redirect variable
     redirect_to = request.GET.get("next", None)
    if redirect_to is not None:
        return redirect(redirect_to)
 
     return redirect_user_to_start_page(request.user)
 