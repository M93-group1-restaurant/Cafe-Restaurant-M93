from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import CartForm, BookTableForm
from home.models import RestaurantInfo
from .models import Order_menuItem, Order, Table, Receipt, Reserve
from menu_items.models import MenuItem
from django.views import View
from django.db.models import Q
from django.contrib import messages
import json


class CartView(View):
    info = RestaurantInfo.objects.first()

    def get(self, request):
        (menuItems, total_price) = CartView.load_cookie(request)
        form = CartForm()
        return render(
            request,
            "cart.html",
            context={
                "info": CartView.info,
                "form": form,
                "menuItems": menuItems,
                "total_price": total_price,
            },
        )

    def post(self, request):
        menuItems, total_price = CartView.load_cookie(request)
        form = CartForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            order = Order.objects.create(table=data["table"], phone_number=data["phone_number"])
            reciept = Receipt.objects.create(
                order=order, total_price=total_price, final_price=total_price
            )
            for menuItem in menuItems:
                Order_menuItem.objects.create(
                    menuItem=menuItem[0], order=order, quantity=menuItem[1]
                )

            request.session["last_order"] = order.id
            if not request.session.get("orders_history"):
                request.session["orders_history"] = [order.id]
            else:
                request.session["orders_history"].append(order.id)

            response = HttpResponseRedirect(reverse("customer"))
            response.delete_cookie("cart")
            return response
        return render(
            request,
            "cart.html",
            context={
                "info": CartView.info,
                "form": form,
                "menuItems": menuItems,
                "total_price": total_price,
            },
        )

    @staticmethod
    def load_cookie(request):
        try:
            order_items = json.loads(request.COOKIES["cart"])
            menuItems = [
                (MenuItem.objects.get(id=i), j["quantity"])
                for i, j in order_items.items()
            ]
            total_price = 0
            for menu_item in menuItems:
                total_price += menu_item[0].price * menu_item[1]
        except:
            menuItems = ()
            total_price = 0
        return (menuItems, total_price)


class CustomerView(View):
    info = RestaurantInfo.objects.first()

    def get(self, request):
        orders_id = request.session.get("orders_history", [])
        orders = [Order.objects.get(id=order_id) for order_id in orders_id]
        return render(
            request,
            "customer.html",
            context={"orders": orders, "info": CustomerView.info},
        )


class BookView(View):
    info = RestaurantInfo.objects.first()

    def get(self, request):
        form = BookTableForm()
        return render(
            request, "book.html", context={"form": form, "info": CartView.info}
        )

    def post(self, request):
        form = BookTableForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tables= Table.objects.filter(capacity__gte=data["number"]).order_by("capacity")
            for table in tables:
                reserves=table.reserves.filter((Q(start_reserve_time__lt=data['end_time']) & Q(start_reserve_time__gte=data['start_time']) & Q(reserve_date=data['date'])) | (Q(end_reserve_time__lte=data['end_time']) & Q(end_reserve_time__gt=data['start_time']) & Q(reserve_date=data['date'])) | (Q(start_reserve_time__lte=data['start_time']) & Q(end_reserve_time__gte=data['end_time']) &  Q(reserve_date=data['date'])))
                if not reserves:
                    selected_table=table
                    break
            else:
                selected_table=None
            if selected_table:
                Reserve.objects.create(phone_number=data['phone_number'], reserve_date=data['date'], start_reserve_time=data['start_time'], end_reserve_time=data['end_time'], table=table)
                messages.success(request, f"Table reservation was done successfully. Table number:{selected_table.number}" )
                return redirect("home")
            messages.error(request, "Sorry. There is no empty table with the capacity and time you want.")
        return render(
            request, "book.html", context={"form": form, "info": CartView.info}
        )
