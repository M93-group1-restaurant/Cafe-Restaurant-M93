from django.db import models
from menu_items.models import MenuItem
from core.models import ModelInfo
from core.utils import get_phonenumber_regex
from datetime import date, datetime
from django.core.exceptions import ValidationError


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
    phone_number = models.CharField(max_length=14, validators=[phone_regex])
    reserve_date = models.DateField()
    start_reserve_time = models.TimeField()
    end_reserve_time = models.TimeField()
    table = models.ForeignKey(
        "Table", on_delete=models.RESTRICT, related_name="reserves"
    )

    def clean(self):
        super().clean()
        if not (date.today() <= self.reserve_date):
            raise ValidationError("Invalid reserve date")
        if (date.today() == self.reserve_date) and (
            self.start_reserve_time < datetime.now().time()
        ):
            raise ValidationError("Invalid start reserve time")
        if not (self.start_reserve_time <= self.end_reserve_time):
            raise ValidationError(
                "End reserve time can't be before start reserve time."
            )


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

    delivery_status = models.IntegerField(
        choices=DeliveryChoice.choices, default=3)
    serving_status = models.IntegerField(
        choices=ServeStatusChoice.choices, default=1)
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

    def get_list_of_order_count_in_month(self):
        list_of_order_count_in_month = [0]*12
        all_orders_in_this_year = Order.objects.filter(
            created_at__year=date.today().year)
        for order_item in all_orders_in_this_year:
            order_created_month = order_item.created_at.month
            list_of_order_count_in_month[order_created_month -
                                         1] = list_of_order_count_in_month[order_created_month-1]+1
        return list_of_order_count_in_month


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

    def get_list_of_menu_item_name_with_quantity(self):
        # list_of_menu_item_name_with_quantity = MenuItem.objects.order_by().values('name').distinct()
        from django.db.models import Sum

        menu_items = Order_menuItem.objects.values(
            'menuItem__title').annotate(total_quantity=Sum('quantity'))
        return menu_items
