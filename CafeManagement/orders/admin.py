from django.contrib import admin
from .models import Order, Receipt, Table, Order_menuItem, Reserve


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    fields = ("number", "space_position", "capacity")
    list_display = ("number", "capacity", "space_position")
    search_fields = ("number",)
    list_filter = ("updated_at",)
    list_per_page = 10


class OrderMenuItemInline(admin.TabularInline):
    model = Order_menuItem
    extra = 3


@admin.register(Reserve)
class ReserveAdmin(admin.ModelAdmin):
    list_display = (
        "table",
        "reserve_date",
        "start_reserve_time",
        "end_reserve_time",
        "phone_number",
    )
    search_fields = ("reserve_date",)
    list_filter = ("updated_at", "reserve_date")
    list_per_page = 10


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "table",
        "serving_status",
    )
    search_fields = ("phone_number", "serving_status")
    list_filter = ("updated_at",)
    radio_fields = {"serving_status": admin.HORIZONTAL}
    list_editable = ("serving_status",)
    inlines = [
        OrderMenuItemInline,
    ]
    list_per_page = 10


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ("order", "total_price", "final_price", "status")
    list_filter = ("updated_at", "status")
    list_editable = ("status",)
    # search_fields = ("order",)
    list_per_page = 10


@admin.register(Order_menuItem)
class Order_menuItemAdmin(admin.ModelAdmin):
    list_display = ("menuItem", "quantity")
    list_filter = ("updated_at", "menuItem")
    # search_fields = ("menuItem",)
    autocomplete_fields = ("menuItem",)
    list_per_page = 10


# admin.site.register(Table, TableAdmin)
# admin.site.register(Order, OrderAdmin)
# admin.site.register(Receipt, ReceiptAdmin)
# admin.site.register(Order_menuItem, Order_menuItemAdmin)
