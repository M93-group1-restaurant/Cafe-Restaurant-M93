# Generated by Django 4.2.2 on 2023-07-01 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_alter_slidercontent_options_slidercontent_number"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="restaurantinfo",
            name="about",
        ),
        migrations.RemoveField(
            model_name="slidercontent",
            name="RestaurantInfo",
        ),
        migrations.DeleteModel(
            name="AboutContent",
        ),
        migrations.DeleteModel(
            name="RestaurantInfo",
        ),
        migrations.DeleteModel(
            name="SliderContent",
        ),
    ]