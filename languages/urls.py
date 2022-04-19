from django.urls import path
from . import views

urlpatterns = [
    path('detail/<language>', views.detail, name="detail")
]