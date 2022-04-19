

from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from .models import Code, Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url="userprofile:login")
def addNewCode(request):
    if request.method == "POST" :
        code = request.POST.get("code")
        title = request.POST.get("title")
        language = request.POST.get("language")

        Code.objects.create(author = request.user,title = title, code = code, code_language = language)

        messages.success(request,"Your code was published successfully")
        return redirect("code:dashboard")
    else:
        return render(request, "addNewCode.html")
@login_required(login_url="userprofile:login")
def dashboard(request):
    codes = Code.objects.filter(author = request.user)
    content = {
        "codes" : codes,
    }
    return render(request, "dashboard.html", content)

@login_required(login_url="userprofile:login")
def updateCode(request, id):
    code = get_object_or_404(Code, id = id)
    
    if request.method == "POST":
        code.code_language = request.POST.get("language")
        code.title = request.POST.get("title")
        code.code = request.POST.get("code")
        code.author = request.user
        code.save()
        messages.success(request, "You updated your code details successfully")
        return redirect("code:dashboard")
    else:
        if request.user == code.author:

            context = {
                "code" : code,
            }
            return render(request, "updateCode.html", context)
        else:
            messages.info(request, "You can not change this code because this doesn't belong to you")
            return redirect("index")



@login_required(login_url="userprofile:login")
def deleteCode(request, id):
    code = get_object_or_404(Code, id = id)
    if code.author == request.user:
        code.delete()
        messages.success(request, "Your code was deleted successfully")
    else:
        messages.info(request, "You can not delete this code...")
    return redirect("code:dashboard")
    

def allCodes(request):
    codes = Code.objects.all()
    context = {
        "codes" : codes
    }
    return render(request, "allCodes.html", context)


def search(request):
    title = request.POST.get("title")
    if title is not None:
        codes = Code.objects.filter(title__contains = title)
    else:
        codes = Code.objects.all()
    context = {
        "codes" : codes
    }
    return render(request, "allCodes.html", context)
    

def detail(request, id):
    code = get_object_or_404(Code, id = id)   
    comments = code.comments.all()
    context = {
        "code" : code,
        "comments": comments,      
    }
    return render(request, "codeDetail.html", context)



@login_required(login_url="userprofile:login")
def addComment(request, id):
    code = get_object_or_404(Code, id = id)
    
    comment_content = request.POST.get("comment")
    
    if comment_content is not None:
        Comment.objects.create(code = code, comment_author = request.user, comment_content = comment_content)
        
        messages.success(request, "You added new comment successfully !")
    else:
        messages.info(request, "You need to write something in textarea for adding comment...")
    return redirect(reverse("code:detail", kwargs={"id" : id}))
    
@login_required(login_url="userprofile:login")
def deleteComment(request, id):
    comment = get_object_or_404(Comment, id = id)
    if comment.comment_author == request.user :
        id = comment.code.id
        comment.delete()
        messages.success(request, "You deleted your comment successfully!")
        return redirect(reverse("code:detail", kwargs={"id" : id}))
    else:
        messages.info(request, "You can not delete another's comment...")
        return redirect("index")
    
