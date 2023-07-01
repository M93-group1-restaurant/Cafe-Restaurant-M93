from django.shortcuts import render
from menu_items.models import MenuItem, Category
from core.models import RestaurantInfo


def home(request):
    menu = MenuItem.objects.all()
    categories = Category.objects.all()
    info = RestaurantInfo.objects.first()
    print(info.opening_hours)
    return render(
        request, "index.html", context={"menu": menu, "categories": categories, "info": info}
    )


def about(request):
    info = RestaurantInfo.objects.first()
    return render(request, "about_page.html", context={"info": info})
