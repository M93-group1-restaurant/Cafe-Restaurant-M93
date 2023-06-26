from django.contrib import admin
from .models import MenuItem, Category, Discount, Comment

admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(Discount)
admin.site.register(Comment)
