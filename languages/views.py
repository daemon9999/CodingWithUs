from django.shortcuts import get_object_or_404, render
from .models import Language
# Create your views here.

def detail(request, language):
    language = get_object_or_404(Language, language = language)
    fields = language.get_list()
    context = {
        "language" : language,
        "fields" : fields
    }

    return render(request,"languageDetail.html", context)