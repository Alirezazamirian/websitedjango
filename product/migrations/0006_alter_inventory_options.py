# Generated by Django 4.2.2 on 2023-06-20 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_inventory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventory',
            options={'verbose_name': 'موجودی انبار', 'verbose_name_plural': 'موجودی انبار ها'},
        ),
    ]
