


from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("addNewCode/", views.addNewCode, name="addNewCode"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path("detail/<int:id>", views.detail, name = "detail"),
    path("delete/<int:id>", views.deleteCode, name = "delete"),
    path("update/<int:id>", views.updateCode, name = "update"),
    path("all/", views.allCodes, name="codes"),
    path("search/", views.search, name = "search"),
    path("addComment/<int:id>", views.addComment, name = "addComment"),
    path("deleteComment/<int:id>", views.deleteComment, name = "deleteComment")

]