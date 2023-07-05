from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView
from .models import CustomUser
from orders.models import Order
from .forms import CashierLoginForm
from django.contrib.auth import authenticate, login
from .backends import PhoneNumberBackend


class CashierPageView(LoginRequiredMixin, TemplateView):
    template_name = 'cashier_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        can_view_custom_user = user.has_perm('app.can_view_custom_user')
        can_edit_custom_user = user.has_perm('app.can_edit_custom_user')
        can_view_orders = user.has_perm('app.can_view_orders')
        can_edit_orders = user.has_perm('app.can_edit_orders')
        can_view_prices = user.has_perm('app.can_view_prices')
        can_edit_prices = user.has_perm('app.can_edit_prices')

        context['user'] = user
        context['can_view_custom_user'] = can_view_custom_user
        context['can_edit_custom_user'] = can_edit_custom_user
        context['can_view_orders'] = can_view_orders
        context['can_edit_orders'] = can_edit_orders
        context['can_view_prices'] = can_view_prices
        context['can_edit_prices'] = can_edit_prices
        return context



class CashierLoginPageView(View):
    template_name = 'cashier_login.html'

    def get(self, request, *args, **kwargs):
        form = CashierLoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = CashierLoginForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            print(phone_number,password)
            user = authenticate(request=request, username=phone_number, password=password)
            print(user)
            if user is not None:
                login(request, user)
            redirect_authenticated_user = True

        error_message = 'Invalid phone number or password. Please try again.'
        return render(request, self.template_name, {'form': form, 'error_message': error_message})