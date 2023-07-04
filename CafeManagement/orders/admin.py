from django.contrib import admin
from .models import Order, Receipt, Table, Order_menuItem


class TableAdmin(admin.ModelAdmin):
    fields = ('number', 'space_position', 'capacity')
    list_display = ('number', 'capacity', 'space_position')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('table', 'serving_status',)


class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('order', 'total_price', 'final_price')


admin.site.register(Table, TableAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Receipt, ReceiptAdmin)
admin.site.register(Order_menuItem)
