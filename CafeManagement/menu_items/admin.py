from django.contrib import admin
from .models import MenuItem, Category
from django.utils.html import format_html


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("updated_at",)
    list_per_page = 10


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = (
        "image_preview",
        "price",
        "category",
        "less_description",
    )
    list_display_links = ("less_description",)
    search_fields = ("title",)
    list_filter = ("updated_at",)
    list_per_page = 8

    @admin.display(description=None)
    def less_description(self, obj):
        return format_html(f'<span style="color:green">{obj.description[:20]}</span>')

    def image_preview(self, obj):
        return format_html(
            '<img src="{}" style="max-height: 100px; max-width: 100px;" />'.format(
                obj.image.url
            )
        )

    image_preview.short_description = "Image Preview"


# admin.site.register(MenuItem, MenuItemAdmin)
# admin.site.register(Category, CategoryAdmin)
