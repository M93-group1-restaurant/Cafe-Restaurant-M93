from django.contrib import admin
from .models import Order, Receipt, Table, Order_menuItem


admin.site.register(Table)
admin.site.register(Order)
admin.site.register(Receipt)
admin.site.register(Order_menuItem)
