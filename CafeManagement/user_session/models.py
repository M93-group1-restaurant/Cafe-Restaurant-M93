from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from datetime import date
from dateutil.relativedelta import relativedelta#pip install python-dateutil


class UserSession(models.Model):
    first_name = models.CharField(150)
    last_name = models.CharField(150)
    phone_number = models.CharField(14)
    birthday = models.DateField(null=True, blank=True, validators=[
            MaxValueValidator(limit_value=date.today()),
            MinValueValidator(limit_value=date.today() - relativedelta(years=100))
        ])
    address = models.CharField(250)
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()

    class Meta:
        ordering = ('-updated_at', '-created_at')
        verbose_name_plural = 'user_sessions'
