# Generated by Django 4.2.2 on 2023-07-08 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0004_alter_order_table"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="end_reserve_date",
        ),
        migrations.RemoveField(
            model_name="order",
            name="start_reserve_date",
        ),
        migrations.AddField(
            model_name="table",
            name="end_reserve_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="table",
            name="start_reserve_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
