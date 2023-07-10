from django.urls import path
from . import views


urlpatterns = [
    path("cashier/", views.cashier.as_view(), name="cashier"),
    path("manager/", views.manager.as_view(), name="manager"),
]
