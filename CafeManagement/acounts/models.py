from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group
from django.db import models
from datetime import timezone
from core.utils import get_phonenumber_regex
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone_regex = get_phonenumber_regex()
    phone_number = models.CharField(
        _("phone number"), max_length=14, unique=True, validators=[phone_regex]
    )

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.phone_number


class CustomGroup(Group):
    # Custom group permissions
    permissions = (
        ("can_view_custom_user", "Can view custom user"),
        ("can_edit_custom_user", "Can edit custom user"),
    )

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        # Create permissions for the group
        for permission in self.permissions:
            name = f"{permission[0]}_{self.name}"
            codename = f"{permission[0]}_{self.name}"
            Permission.objects.update_or_create(
                name=name,
                codename=codename,
                defaults={
                    "content_type_id": ContentType.objects.get_for_model(CustomUser).pk,
                },
            )
        super().save(*args, **kwargs)
