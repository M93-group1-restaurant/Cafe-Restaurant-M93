from django.shortcuts import render, redirect
from .forms import BookTableForm
from core.models import RestaurantInfo


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
