from django.db import models
from menu_items.models import MenuItem


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
    class DeliveryChoice(models.IntegerChoices):
        TAKE = 1, "Come to take 🚶‍♂️"
        SEND = 2, "Send 🚚"
        EAT = 3, "Eat 🍽️"

    class ServeStatusChoice(models.IntegerChoices):
        CANCEL = 1, "PENDING 🔁"
        COOKING = 2, "CONFIRM ✔"
        POSTPONE = 3, "COOKING 🍔"
        SERVED = 4, "SERVED 🤤"
        CONFIRM = 5, "CANCEL ❌"

    table = models.ForeignKey(
        "Table", on_delete=models.SET_NULL, related_name="orders", null=True, blank=True
    )
    delivery_status = models.IntegerField(
        choices=DeliveryChoice.choices)
    serving_status = models.IntegerField(
        choices=ServeStatusChoice.choices)
    start_reserve_date = models.DateTimeField(null=True, blank=True)
    end_reserve_date = models.DateTimeField(null=True, blank=True)
    phone_number = models.CharField(max_length=14, null=True, blank=True)

    # userSession = models.ForeignKey(
    #     UserSession,
    #     on_delete=models.SET_NULL,
    #     related_name="orders",
    #     blank=True,
    #     null=True,
    # )

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
