from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    url(r'^dashboard/admin/users/add_user/$', views.add_user, name='add_user'),
]
