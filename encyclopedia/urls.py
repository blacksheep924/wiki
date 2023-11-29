from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.title, name="title"),
    path("error", views.error, name="error"),
    path("search", views.search, name="search"),
    
    
]
