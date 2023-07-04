from django.contrib import admin
from .models import MenuItem, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)





admin.site.register(MenuItem)
admin.site.register(Category, CategoryAdmin)
