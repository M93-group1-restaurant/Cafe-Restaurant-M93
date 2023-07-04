from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from datetime import date
from dateutil.relativedelta import relativedelta # pip install python-dateutil


class UserSession(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=14)
    birthday = models.DateField(
        null=True,
        blank=True,
        validators=[
            MaxValueValidator(limit_value=date.today()),
            MinValueValidator(limit_value=date.today() - relativedelta(years=100)),
        ],
    )
    address = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-updated_at", "-created_at")
        verbose_name_plural = "user_sessions"
