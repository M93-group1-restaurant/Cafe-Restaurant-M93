from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import CartForm, BookTableForm
from home.models import RestaurantInfo
from .models import Order_menuItem, Order, Table
from menu_items.models import MenuItem
from django.views import View
import json


class CartView(View):
    info = RestaurantInfo.objects.first()

    def get(self,request):
        (menuItems,total_price)=CartView.load_cookie(request)
        form=CartForm()
        return render(request, "cart.html", context={"info": CartView.info, "form":form, "menuItems": menuItems, "total_price":total_price})

    def post(self,request):
        menuItems,total_price=CartView.load_cookie(request)
        form=CartForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if data['table_number']:
                table=Table.objects.get(number=data['table_number'])
            else:
                table=None
            order = Order.objects.create(table=table, phone_number=data['phone_number'])
            for menuItem in menuItems:
                Order_menuItem.objects.create(
                    menuItem=menuItem[0], order=order, quantity=menuItem[1]
                )
            response = HttpResponseRedirect(reverse("home"))
            response.delete_cookie("cart")
            request.session['last_order']=order.id
            if not request.session.get('orders_history'):
                request.session['orders_history']=[order.id]
            else:
                request.session['orders_history'].append(order.id)
            return response
        return render(request, "cart.html", context={"info": CartView.info, "form":form, "menuItems": menuItems, "total_price":total_price})

        
    @classmethod
    def load_cookie(cls,request):
        try:
            order_items = json.loads(request.COOKIES["cart"])
            menuItems=[(MenuItem.objects.get(id=i),j["quantity"]) for i,j in order_items.items()]
            total_price=0
            for menu_item in menuItems:
                total_price+=menu_item[0].price*menu_item[1]
        except:
            menuItems=()
            total_price=0
        return (menuItems,total_price)
        

class BookView(View):
    info = RestaurantInfo.objects.first()

    def get(self,request):
        form = BookTableForm()
        return render(request, "book.html", context={"form": form, "info": CartView.info})
    
    def post(self,request):
        form = BookTableForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            return redirect("home")
        return render(request, "book.html", context={"form": form, "info": CartView.info})
        