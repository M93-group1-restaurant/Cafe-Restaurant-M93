from django.urls import path
from . import views


urlpatterns = [
    path("cart/", views.CartView.as_view(), name="cart"),
    path("customer/", views.CustomerView.as_view(), name="customer"),
    path("book/", views.BookView.as_view(), name="book"),
]
