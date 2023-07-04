from django.contrib import admin
from django.urls import path
from . import views

# Django admin customization
admin.site.header = "Caffe Restaurant"
urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
]
