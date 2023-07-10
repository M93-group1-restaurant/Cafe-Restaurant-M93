from django.urls import path
from . import views


urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("cashier/", views.CashierView.as_view(), name="cashier"),
    path("manager/", views.ManagerView.as_view(), name="manager"),
]
