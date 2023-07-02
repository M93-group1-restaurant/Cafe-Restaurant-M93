from django.shortcuts import render, redirect
from .forms import CartForm, BookTableForm
from home.models import RestaurantInfo
import json


def cart(request):
    if request.method == "POST":
        try:
            order_items=json.loads(request.COOKIES["cart"])
        except:
            order_items={}
        print(order_items)

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
