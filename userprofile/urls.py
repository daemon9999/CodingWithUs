from django.urls import path
from . import views

urlpatterns =[
    path("register/", views.registerUser, name = "register"),
    path("login/", views.loginUser, name = "login"),
    path("logout/", views.logoutUser, name = "logout"),
    path("updateUsername/", views.updateUsername, name = "updateUsername"),
    path("updatePassword/", views.updatePassword, name = "updatePassword"),
    path("profileDetail/", views.profileDetail, name = "profileDetail"),
    path("updateAbout/<int:id>", views.updateAbout, name="updateAbout"),
    path("profile/<int:id>", views.profile, name = "profile" ),

    
]