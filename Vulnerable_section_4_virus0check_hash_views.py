     else:
         form=FileUploadForm()
     return render(request, 'virus0check/upload.html', {'form': form})


def index(request):  # HttpRequest
    return render(request, 'index.html')


def result(request):
    return HttpResponse("Hash result page")
\ No newline at end of file