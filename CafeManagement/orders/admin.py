from django.contrib import admin
from .models import Order, Receipt, Table, MenuItem

admin.site.register(Order)
admin.site.register(Receipt)
admin.site.register(Table)
admin.site.register(MenuItem)
