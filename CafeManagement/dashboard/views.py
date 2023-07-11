from django.shortcuts import render, redirect
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
    PermissionRequiredMixin,
)
from django.views import View
from orders.models import Order, Receipt
from menu_items.models import MenuItem
from django.http import Http404



class DashboardView(LoginRequiredMixin, UserPassesTestMixin, View):

    login_url = "/login/"

    def test_func(self):
        result = (
            self.request.user.groups.filter(name="cashier").exists()
            or self.request.user.groups.filter(name="manager").exists()
        )
        if not result:
            raise Http404
        return result

    def get(self, request):
        orders = Order.objects.all()
        menuItems = MenuItem.objects.all()
        reciepts = Receipt.objects.all()
        return render(
            request,
            "dashboard/index.html",
            context={"orders": orders, "menuItems": menuItems, "reciepts": reciepts},
        )

    def post(self, request):
        ...


# class ManagerView(LoginRequiredMixin, PermissionRequiredMixin, View):

#     login_url = '/login/'
#     redirect_field_name = 'redirect_to'

#     def dispatch(self, *args, **kwargs):
#         if not self.request.user.is_authenticated:
#             return redirect(self.login_url)
#         elif not (
#             self.request.user.groups.filter(name="manager").exists()
#         ):
#             raise Http404
#         return super(ManagerView, self).dispatch(*args, **kwargs)

#     def get(self, request):
#         reciepts = Receipt.objects.all()
#         return render(request, 'manager.html', context={"reciepts":reciepts})
