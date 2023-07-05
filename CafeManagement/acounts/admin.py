from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomGroup, CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("phone_number", "is_staff", "is_active",)
    list_filter = ("phone_number", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("phone_number", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "phone_number", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("phone_number",)
    ordering = ("phone_number",)
    def save_model(self, request, obj, form, change):
        # Assign the custom group to the user
        group_name = 'Cashier'  # Update with the name of the cashier group
        group, _ = CustomGroup.objects.get_or_create(name=group_name)
        obj.groups.set([group])

        super().save_model(request, obj, form, change)

admin.site.register(CustomUser, CustomUserAdmin)