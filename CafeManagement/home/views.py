from django.shortcuts import render, redirect
from menu_items.models import MenuItem, Category
from core.models import RestaurantInfo
from django.contrib.auth.decorators import login_required


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

def signup(request):
    if request.method == 'POST' :
        form = SignUpForm(request.POST)
        if form.is_valid():
            user= form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.first_name = form.cleaned_data['firstname']
            user.last_name = form.cleaned_data['lastname']
            user.email = form.cleaned_data['email']
            user.username = user.email.split('@')[0]
            user.set_password(form.cleaned_data['password'])
            user.save()
            address = form.cleaned_data['address']
            contact = form.cleaned_data['contact']
            customer = Customer.objects.create(customer=user, address=address, contact=contact)
            customer.save()
            return redirect('http://localhost:8000/accounts/login/')
    
    else:
        form = SignUpForm()
        
    return render(request, 'registration/signup.html', {'form': form})