from django.urls import path
from . import views

urlpatterns = [
    path("menu/", views.MenuView.as_view(), name="menu"),
]
