# Generated by Django 4.2.2 on 2023-06-20 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_rename_inventory_quantity_inventory_quantity'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='inventory',
            unique_together={('product', 'store')},
        ),
    ]
