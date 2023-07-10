from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import View
from orders.models import Order, Receipt
from menu_items.models import MenuItem


class CashierView(LoginRequiredMixin, PermissionRequiredMixin, View):
    # permission_required = "acounts."
    def get(self, request):
        orders = Order.objects.all()
        menuItems = MenuItem.objects.all()
        return render(request, 'cashier.html', context={"orders":orders, "menuItems": menuItems})
    
    def post(self, request):
        ...


class ManagerView(LoginRequiredMixin, PermissionRequiredMixin, View):
    # permission_required = "acounts."
    def get(self, request):
        reciepts = Receipt.objects.all()
        return render(request, 'manager.html', context={"reciepts":reciepts})

