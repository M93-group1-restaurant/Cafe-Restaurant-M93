from django.contrib import admin
from .models import Order, Reciept, Table, Table_order

admin.site.register(Order)
admin.site.register(Reciept)
admin.site.register(Table)
admin.site.register(Table_order)