from django.db import models
from datetime import timedelta
from core.models import ModelInfo

class Customer(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    contact = models.CharField(max_length = 10)
    orders = models.IntegerField(default=0)
    total_sale = models.IntegerField(default=0)
class Category(ModelInfo):
    name = models.CharField(max_length=150)
    parent_category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        related_name="categories",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class MenuItem(ModelInfo):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name="menuItems",
        null=True,
        blank=True,
    )
    period_time_service = models.DurationField(default=timedelta(seconds=300))
    estimated_cooking_time = models.DurationField(default=timedelta(seconds=300))
    image = models.ImageField(upload_to="images/", default="", null=True, blank=True)
    is_active = models.BooleanField(default=True)
    description = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = "MenuItems"

    def __str__(self):
        return self.title