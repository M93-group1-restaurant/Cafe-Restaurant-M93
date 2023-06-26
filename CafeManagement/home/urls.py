from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index.html', views.home, name='home'),
    path('menu.html', views.menu, name='menu'),
    path('about.html', views.about, name='about'),
    path('book.html', views.book, name='book'),
]

