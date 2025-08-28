 from django.shortcuts import render, redirect, get_object_or_404
 from django.http import Http404, FileResponse
 from django.utils import translation

 from .models import *
 
 def generate_menu_context(request):
         'contest_languages': contest_languages,
     })
 

 def toggle_lang(request):
     lang = 'tr' if translation.get_language() == 'en' else 'en'

     request.session[translation.LANGUAGE_SESSION_KEY] = lang
 
    return redirect(request.GET.get('next', '/'))