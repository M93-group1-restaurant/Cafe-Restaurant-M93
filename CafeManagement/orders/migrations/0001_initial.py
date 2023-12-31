# Generated by Django 4.2.2 on 2023-07-12 22:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("menu_items", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "delivery_status",
                    models.IntegerField(
                        choices=[
                            (1, "Come to take 🚶\u200d♂️"),
                            (2, "Send 🚚"),
                            (3, "Eat 🍽️"),
                        ],
                        default=3,
                    ),
                ),
                (
                    "serving_status",
                    models.IntegerField(
                        choices=[
                            (1, "PENDING ⌚"),
                            (2, "CONFIRM ✔"),
                            (3, "COOKING 🍔"),
                            (4, "SERVED 🤤"),
                            (5, "CANCEL ❌"),
                        ],
                        default=1,
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(
                        blank=True,
                        max_length=14,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="invalid phone number",
                                regex="^(\\+?|0*)(98)?9[\\d-]{9,}$",
                            )
                        ],
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Orders",
            },
        ),
        migrations.CreateModel(
            name="Table",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("number", models.IntegerField()),
                ("space_position", models.CharField(max_length=250)),
                ("capacity", models.PositiveIntegerField()),
            ],
            options={
                "verbose_name_plural": "Tables",
            },
        ),
        migrations.CreateModel(
            name="Reserve",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "phone_number",
                    models.CharField(
                        max_length=14,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="invalid phone number",
                                regex="^(\\+?|0*)(98)?9[\\d-]{9,}$",
                            )
                        ],
                    ),
                ),
                ("reserve_date", models.DateField()),
                ("start_reserve_time", models.TimeField()),
                ("end_reserve_time", models.TimeField()),
                (
                    "table",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="reserves",
                        to="orders.table",
                    ),
                ),
            ],
            options={
                "ordering": ("-updated_at", "-created_at"),
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Receipt",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("total_price", models.IntegerField()),
                ("final_price", models.IntegerField()),
                (
                    "status",
                    models.IntegerField(
                        blank=True,
                        choices=[(1, "UNPAID ⌚"), (2, "PAID 💲"), (3, "CANCEL ❌")],
                        default=1,
                        null=True,
                    ),
                ),
                (
                    "order",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="receipt",
                        to="orders.order",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Receipts",
            },
        ),
        migrations.CreateModel(
            name="Order_menuItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("quantity", models.PositiveIntegerField()),
                (
                    "menuItem",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="orders",
                        to="menu_items.menuitem",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="menuItems",
                        to="orders.order",
                    ),
                ),
            ],
            options={
                "ordering": ("-updated_at", "-created_at"),
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="order",
            name="table",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="orders",
                to="orders.table",
            ),
        ),
    ]
