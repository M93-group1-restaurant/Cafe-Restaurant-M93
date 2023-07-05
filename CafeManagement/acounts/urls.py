from django.urls import path
from .views import CashierPageView, CashierLoginPageView

app_name = 'acounts'  
urlpatterns = [
    path('cashier/', CashierPageView.as_view(), name='cashier_page'),
    path('cashier/login/', CashierLoginPageView.as_view(), name='cashier_login'),
]
