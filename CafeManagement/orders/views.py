from django.shortcuts import render, redirect
from .forms import CartForm, BookTableForm
from home.models import RestaurantInfo
from .models import Order_menuItem, Order
from menu_items.models import MenuItem
import json


def cart(request):
    if request.method == "POST":
        try:
            order_items = json.loads(request.COOKIES["cart"])
            order = Order.objects.create()
            for (i, j) in order_items.items():
                menuItem = MenuItem.objects.get(id=i)
                Order_menuItem.objects.create(
                    menuItem=menuItem, order=order, quantity=j["quantity"]
                )
        except:
            order_items = {}
        return redirect("home")

    info = RestaurantInfo.objects.first()
    return render(request, "cart.html", context={"info": info})


def book(request):
    info = RestaurantInfo.objects.first()
    if request.method == "POST":
        form = BookTableForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            return redirect("home")

    else:
        form = BookTableForm()
    return render(request, "book.html", context={"form": form, "info": info})
