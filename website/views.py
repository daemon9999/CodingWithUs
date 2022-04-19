from django.shortcuts import render

from languages.models import Language

def index(request):
    languages = Language.objects.all()
    context = {
        "languages" : languages
    }
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")


