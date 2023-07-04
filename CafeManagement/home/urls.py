from django.contrib import admin
from django.urls import path
from . import views

# Django admin customization
admin.site.site_header = "Login to Caffe Restaurant"
admin.site.site_title = "Welcome to Caffe Restaurant"
admin.site.index_title = "Welcome to Group one Caffe Restaurant Portal"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
]
