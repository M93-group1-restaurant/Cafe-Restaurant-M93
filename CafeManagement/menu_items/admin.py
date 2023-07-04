from django.contrib import admin
from .models import MenuItem, Category
from django.utils.html import format_html


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


# def show_image(obj):
#     return format_html(f'<img src="obj.image" alt="sss" width="500" height="600">')


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('price', 'category', 'less_description',)
    list_display_links = ('less_description',)

    @admin.display(description=None)
    def less_description(self, obj):
        return format_html(f'<span style="color:green">{obj.description[:20]}</span>')



admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Category, CategoryAdmin)
