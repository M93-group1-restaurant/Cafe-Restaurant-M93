from django.contrib import admin
from .models import Order, Receipt, Table, Order_menuItem


class TableAdmin(admin.ModelAdmin):
    fields = ('number', 'space_position', 'capacity')
    list_display = ('number', 'capacity', 'space_position')


admin.site.register(Table, TableAdmin)
admin.site.register(Order)
admin.site.register(Receipt)
admin.site.register(Order_menuItem)
