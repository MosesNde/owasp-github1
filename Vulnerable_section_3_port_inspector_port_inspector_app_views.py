         user.is_email_verified = True
         user.save()
         messages.success(request, "Your email has been verified.")
        return redirect("verify-email-complete")
     else:
         messages.warning(request, "The link is invalid.")
     return render(request, "verify-email-confirm.html")