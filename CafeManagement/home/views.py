from django.shortcuts import render, redirect
from menu_items.models import MenuItem, Category
from core.models import RestaurantInfo
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

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

@login_required
@staff_member_required
def users_admin(request):
    customers = Customer.objects.filter()
    print(customers)
    return render(request, 'admin_temp/users.html', {'users':customers})

@login_required
@staff_member_required
def add_user(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        contact = request.POST['contact']
        email = request.POST['email']
        password = request.POST['password']
        confirm_pass = request.POST['confirm_password']
        username = email.split('@')[0]
    
        if (first_name == "") or (last_name == "") or (address == "") or (contact == "") or (email == "") or (password == "") or (confirm_pass == ""):
                customers = Customer.objects.filter()
                error_msg = "Please enter valid details"
                return render(request, 'admin_temp/users.html', {'users': customers, 'error_msg': error_msg})

        if password == confirm_pass:
            user = User.objects.create(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
            user.save()
            cust = Customer.objects.create(customer=user, address=address, contact=contact)
            cust.save()
            success_msg = "New user successfully created"
            customers = Customer.objects.filter()
            return render(request, 'admin_temp/users.html', {'users': customers, 'success_msg': success_msg})

    return redirect('hotel:users_admin')