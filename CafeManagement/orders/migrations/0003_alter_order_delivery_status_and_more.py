# Generated by Django 4.2.2 on 2023-07-02 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0002_alter_order_delivery_status_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="delivery_status",
            field=models.IntegerField(
                choices=[(1, "Come to take 🚶\u200d♂️"), (2, "Send 🚚"), (3, "Eat 🍽️")],
                default=3,
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="serving_status",
            field=models.IntegerField(
                choices=[
                    (1, "CANCEL ❌"),
                    (2, "COOKING 🍔"),
                    (3, "POSTPONE 🔁"),
                    (4, "SERVED 🤤"),
                    (5, "PENDING ⌚"),
                ],
                default=5,
            ),
        ),
        migrations.AlterField(
            model_name="order_menuitem",
            name="order",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="menuItems",
                to="orders.order",
            ),
        ),
    ]