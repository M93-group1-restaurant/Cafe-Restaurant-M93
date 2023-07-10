from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from orders.models import Order, Receipt
from menu_items.models import MenuItem
from core.utils import is_member


class CashierView(LoginRequiredMixin, UserPassesTestMixin, View):
    
    def test_func(self):
        result= is_member(self.request.user, "cashier") or is_member(self.request.user, "manager")
        return result

    def get(self, request):
        orders = Order.objects.all()
        menuItems = MenuItem.objects.all()
        return render(request, 'cashier.html', context={"orders":orders, "menuItems": menuItems})
    
    def post(self, request):
        ...


class ManagerView(LoginRequiredMixin, UserPassesTestMixin, View):

    def test_func(self):
        return is_member(self.request.user, "manager")

    def get(self, request):
        reciepts = Receipt.objects.all()
        return render(request, 'manager.html', context={"reciepts":reciepts})

