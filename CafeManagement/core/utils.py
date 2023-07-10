from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


def get_phonenumber_regex():
    phone_regex = RegexValidator(
        regex=r"^(\+?|0*)(98)?9[\d-]{9,}$", message=_("invalid phone number")
    )
    return phone_regex


def is_member(user, group_name):
    return user.groups.filter(name=group_name).exists()