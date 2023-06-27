from django.contrib import admin
from .models import MenuItem, Category

if admin.site.is_registered(MenuItem):
    admin.site.unregister(MenuItem)

admin.site.register(MenuItem)
admin.site.register(Category)
