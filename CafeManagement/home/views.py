from django.shortcuts import render
from menu_items.models import MenuItem, Category


def home(request):
    menu=MenuItem.objects.all()
    categories=Category.objects.all()
    return render(request, 'index.html', context={"menu":menu,"categories":categories})

def about(request):
    return render(request, 'about.html')