# Generated by Django 4.2.2 on 2023-07-01 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_alter_aboutcontent_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="slidercontent",
            name="button_link",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="slidercontent",
            name="button_text",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
