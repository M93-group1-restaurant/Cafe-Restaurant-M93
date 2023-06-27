from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index.html', views.home, name='home'),
    path('about.html', views.about, name='about'),
    path('book.html', views.book, name='book'),
    path('', include('menu_items.urls'))
]

