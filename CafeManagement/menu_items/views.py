from django.shortcuts import render
from .models import MenuItem, Category
from home.models import RestaurantInfo


def menu(request):
    menu = MenuItem.objects.all()
    categories = Category.objects.all()
    info = RestaurantInfo.objects.first()

    return render(
        request, "menu_page.html", context={"menu": menu, "categories": categories, "info": info}
    )
