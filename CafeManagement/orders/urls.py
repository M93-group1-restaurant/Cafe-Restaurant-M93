from django.urls import path
from . import views


urlpatterns = [
    path("cart/", views.CartView.as_view(), name="cart"),
    path("book/", views.BookView.as_view(), name="book"),
]
