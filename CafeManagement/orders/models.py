from django.db import models
from menu_items.models import MenuItem
from core.models import ModelInfo
from core.utils import get_phonenumber_regex


class Table(ModelInfo):

    number = models.IntegerField()
    space_position = models.CharField(max_length=250)
    capacity = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "Tables"

    def __str__(self):
        return f"table {self.number}"


class Reserve(ModelInfo):
    phone_regex = get_phonenumber_regex()
    phone_number = models.CharField(
        max_length=14, validators=[phone_regex]
    )
    reserve_date = models.DateField()
    start_reserve_time = models.TimeField()
    end_reserve_time = models.TimeField()
    table = models.ForeignKey("Table", on_delete = models.RESTRICT, related_name="reserves")


class Order(ModelInfo):
    class DeliveryChoice(models.IntegerChoices):
        TAKE = 1, "Come to take 🚶‍♂️"
        SEND = 2, "Send 🚚"
        EAT = 3, "Eat 🍽️"

    class ServeStatusChoice(models.IntegerChoices):
        PENDING = 1, "PENDING ⌚"
        CONFIRM = 2, "CONFIRM ✔"
        COOKING = 3, "COOKING 🍔"
        SERVED = 4, "SERVED 🤤"
        CANCEL = 5, "CANCEL ❌"

    table = models.ForeignKey(
        "Table", on_delete=models.SET_NULL, related_name="orders", null=True
    )

    delivery_status = models.IntegerField(choices=DeliveryChoice.choices, default=3)
    serving_status = models.IntegerField(choices=ServeStatusChoice.choices, default=1)
    phone_regex = get_phonenumber_regex()
    phone_number = models.CharField(
        max_length=14, null=True, blank=True, validators=[phone_regex]
    )
    # userSession = models.ForeignKey(
    #     UserSession,
    #     on_delete=models.SET_NULL,
    #     related_name="orders",
    #     blank=True,
    #     null=True,
    # )

    class Meta:
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"order id:{self.id} status:{self.serving_status}"


class Receipt(ModelInfo):
    class ConfirmStatusChoice(models.IntegerChoices):
        UNPAID = 1, "UNPAID ⌚"
        PAID = 2, "PAID 💲"
        CANCEL = 3, "CANCEL ❌"

    order = models.OneToOneField(
        Order, on_delete=models.SET_NULL, related_name="receipt", null=True, blank=True
    )
    total_price = models.IntegerField()
    final_price = models.IntegerField()
    status = models.IntegerField(
        choices=ConfirmStatusChoice.choices, default=1, null=True, blank=True
    )

    class Meta:
        verbose_name_plural = "Receipts"

    def __str__(self):
        return f"order {self.order} {self.final_price}"


class Order_menuItem(ModelInfo):
    menuItem = models.ForeignKey(
        MenuItem,
        on_delete=models.SET_NULL,
        related_name="orders",
        null=True,
        blank=True,
    )
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="menuItems", null=True, blank=True
    )
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.order}, {self.menuItem}"
