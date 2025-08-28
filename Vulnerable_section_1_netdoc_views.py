             }
             utils.spawn_script("Discover", user=request.user, post_data=data)
 
            return_url = form.cleaned_data.get("return_url")
            if return_url and return_url.startswith("/"):
                return redirect(return_url)
             return redirect(self.get_return_url(request, obj))
 
         logger.debug("Form validation failed")