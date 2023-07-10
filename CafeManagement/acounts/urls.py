from django.urls import path
from . import views


urlpatterns = [
    path("cashier/", views.CashierView.as_view(), name="cashier"),
    path("manager/", views.ManagerView.as_view(), name="manager"),
]
