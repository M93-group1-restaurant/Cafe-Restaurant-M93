from django.shortcuts import render
from .models import MenuItem, Category

def menu(request):
    menu=MenuItem.objects.all()
    categories=Category.objects.all()

    return render(request, "menu_page.html", context={"menu":menu,"categories":categories})
