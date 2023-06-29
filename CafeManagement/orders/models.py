from django.db import models
from menu_items.models import MenuItem
from user_session.models import UserSession


class ModelInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ("-updated_at", "-created_at")


class Table(ModelInfo):
    number = models.IntegerField()
    space_position = models.CharField(max_length=250)
    capacity = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "Tables"


class Order(ModelInfo):
    class DeliveryChoice(models.TextChoices):
        TAKE = "C", "COME TO TAKE"
        SEND = "S", "SEND"
        EAT = "E", "EAT"

    table = models.ForeignKey(
        "Table", on_delete=models.SET_NULL, related_name="orders", null=True, blank=True
    )
    delivery_status = models.CharField(
        choices=DeliveryChoice.choices, max_length=20)
    start_reserve_date = models.DateTimeField(null=True, blank=True)
    end_reserve_date = models.DateTimeField(null=True, blank=True)
    userSession = models.ForeignKey(
        UserSession,
        on_delete=models.SET_NULL,
        related_name="orders",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name_plural = "Orders"


class Receipt(ModelInfo):
    order = models.OneToOneField(
        Order, on_delete=models.SET_NULL, related_name="receipt", null=True, blank=True
    )
    total_price = models.IntegerField()
    final_price = models.IntegerField()

    class Meta:
        verbose_name_plural = "Receipts"


class Order_menuItem(ModelInfo):
    menuItem = models.ForeignKey(
        MenuItem,
        on_delete=models.SET_NULL,
        related_name="orders",
        null=True,
        blank=True,
    )
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="menuItems"
    )
    quantity = models.PositiveIntegerField()
