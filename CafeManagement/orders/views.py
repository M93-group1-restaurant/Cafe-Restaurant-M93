from django.shortcuts import render, redirect
from .forms import CartForm, BookTableForm
from home.models import RestaurantInfo


def cart(request):
    info = RestaurantInfo.objects.first()
    if request.method == "POST":
        form = CartForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
        return redirect("home")
    else:
        form = CartForm()
    return render(request, "cart.html", context={"form":form, "info": info})


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
