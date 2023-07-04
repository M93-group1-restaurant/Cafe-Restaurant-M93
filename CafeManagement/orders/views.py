from django.shortcuts import render, redirect
from .forms import CartForm, BookTableForm
from home.models import RestaurantInfo
from .models import Order_menuItem, Order
from menu_items.models import MenuItem
import json
from functools import reduce


def cart(request):
    try:
        order_items = json.loads(request.COOKIES["cart"])
        menuItems=[(MenuItem.objects.get(id=i),j["quantity"]) for i,j in order_items.items()]
        total_price=0
        # for menu_item in menuItems:
        #     total_price+=menu_item[0].price*menu_item[1]
        total_price = reduce(lambda x,y : x[0].price*x[1]+y[0].price*y[1],menuItems)
    except:
        order_items = {}
        menuItems=()
        total_price=0
    if request.method == "POST":
        order = Order.objects.create()
        for menuItem in menuItems:
            Order_menuItem.objects.create(
                menuItem=menuItem[0], order=order, quantity=menuItem[1]
            )
        return redirect("home")
    info = RestaurantInfo.objects.first()
    return render(request, "cart.html", context={"info": info, "menuItems": menuItems, "total_price":total_price})


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
