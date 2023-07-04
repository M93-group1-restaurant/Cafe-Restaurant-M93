from django.contrib import admin
from .models import MenuItem, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('image', 'price', 'category')


admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Category, CategoryAdmin)
