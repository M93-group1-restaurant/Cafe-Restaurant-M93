from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')
