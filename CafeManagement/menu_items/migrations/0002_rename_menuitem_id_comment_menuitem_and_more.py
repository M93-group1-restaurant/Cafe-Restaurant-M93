# Generated by Django 4.2.2 on 2023-06-27 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu_items', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='menuItem_id',
            new_name='menuItem',
        ),
        migrations.RenameField(
            model_name='menuitem',
            old_name='Category_id',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='menuitem',
            old_name='discount_id',
            new_name='discount',
        ),
        migrations.RemoveField(
            model_name='category',
            name='Category_id',
        ),
        migrations.AddField(
            model_name='category',
            name='parent_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu_items.category'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
