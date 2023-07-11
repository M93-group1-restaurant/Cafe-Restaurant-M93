from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
    PermissionRequiredMixin,
)
from django.views import View
from orders.models import Order, Receipt
from menu_items.models import MenuItem
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm


class LoginView(View):
    template_name = "acounts/login.html"

    def get(self, request, *args, **kwargs):

        form = LoginForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        redirect_to = request.POST.get("next", "")
        form = LoginForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data["phone_number"]
            password = form.cleaned_data["password"]
            user = authenticate(
                request=request, username=phone_number, password=password
            )
            if user:
                login(request, user)
                if redirect_to:
                    return HttpResponseRedirect(redirect_to)
                return HttpResponseRedirect(reverse("home"))

        error_message = "Invalid phone number or password. Please try again."
        return render(
            request, self.template_name, {"form": form, "error_message": error_message}
        )


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("login"))


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
            "acounts/dashboard.html",
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
