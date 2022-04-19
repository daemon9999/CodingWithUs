
import re
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse


from .models import Detail
# Create your views here.


def registerUser(request):
    if request.user.is_authenticated:
        messages.info(request, "You have already logged in, you need to log out in order to register...")
        return redirect("index")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            password_confirm = request.POST.get("password_confirm")

            try:
                control_username = get_object_or_404(User, username = username)
                if control_username is not None:
                    messages.info(request, "This name was taken.. Please, Try Again")
                    return redirect("userprofile:register")
            except:
                if password != password_confirm :
                    messages.info(request, "Passwords entered are not the same...")
                    return redirect("userprofile:register")
                else:
                    newUser = User(username = username, email = email)
                    newUser.set_password(password)
                    newUser.save()
                    login(request, newUser)
                    messages.success(request, "You created new account successfully!")
                    return redirect("index")
                    
        else:
            return render(request, "register.html")


def loginUser(request):
    if request.user.is_authenticated:
        messages.info(request,"You have already logged in, you need to log out in order to log in another account...")
        return redirect("index")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = authenticate(request, username = username, email = email, password = password)
            if user is None:
                messages.info(request, "Something was entered wrong or This account was not created...")
                return redirect("userprofile:login")
            else:
                login(request, user)
                
                if "next" in request.POST:
                    return redirect(request.POST.get("next"))
                else:    
                    messages.success(request, "You entered your account successfully!")
                    return redirect("index")
        else:
            return render(request, "login.html")



def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "You logged out succesfully!")
        return redirect("index")
        
    else:
        messages.info(request, "You have not logged in for logging out...")
        return redirect("index")

@login_required(login_url="userprofile:login")
def updateUsername(request):
    if request.method == "POST":
        newUsername = request.POST.get("newUsername")
        try:
            controlNewUsername = get_object_or_404(User, username = newUsername)
            if controlNewUsername is not None:
                messages.info(request,"This username was taken...")
                return redirect("userprofile:updateUsername")
        except:
            user = User.objects.get(username = request.user.username)
            user.username = newUsername
            user.save()

            messages.success(request, "You changed your username successfully!")
            return redirect("index")
    else:
        return render(request, "updateUsername.html")

@login_required(login_url="userprofile:login")
def updatePassword(request):
    if request.method == "POST":
        previousPassword = request.POST.get("previousPassword")
        newPassword = request.POST.get("newPassword")
        confirmNewPassword = request.POST.get("confirmNewPassword")
        user = User.objects.get(username = request.user.username)
        
        if user.check_password(previousPassword):
            if previousPassword == newPassword :
                messages.info(request, "Your previous and new passwords are the same... Please, enter a new password")
                return redirect("userprofile:updatePassword")
            elif newPassword != confirmNewPassword :
                messages.info(request, "New passwords entered are not the same... Please, try again")
                return redirect("userprofile:updatePassword")
            else:
                user.set_password(newPassword)
                user.save()
                login(request, user)
                messages.success(request, "You changed your password successfully!")
                return redirect("index")
        else:
            messages.info(request, "Previous Password entered is not correct... Please, Try Again")
            return redirect("userprofile:updatePassword")
    else:
        return render(request, "updatePassword.html")

@login_required(login_url="userprofile:login")
def profileDetail(request):
    user = User.objects.get(username = request.user.username)
    
    codes = user.codes.all()
    codesCount = len(codes)
    about = user.about.all().first()
    context = {
        "user" : user,
        "codesCount" : codesCount,
        "about" : about,
    }
    return render(request, "profileDetail.html", context)


@login_required(login_url="userprofile:login")
def updateAbout(request, id):
    
    about = request.POST.get("about")
    user = get_object_or_404(User, id = id)
    if user == request.user:
        if about is not None:
            detail = user.about.all()
            if detail is not None:
                detail.delete()
            Detail.objects.create(user = request.user, about = about)
            messages.success(request, "You changed some information about you successfully!")
        else:
            messages.info(request, "You should write something in textarea for changing information about you...")
    else:
        messages.info("You don't have any access to another user's profile...")

    return redirect("userprofile:profileDetail")
    

def profile(request, id):
    user = get_object_or_404(User, id = id)
    about = user.about.all().first()
    codes = user.codes.all()
    codesCount = len(codes)
    context = {
        "user" : user,
        "about" : about,
        "codesCount" : codesCount,
    }
    return render(request, "profile.html", context)