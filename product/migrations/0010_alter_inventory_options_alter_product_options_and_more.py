# Generated by Django 4.2.2 on 2023-06-21 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_inventory_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventory',
            options={'verbose_name': 'موجودی انبار', 'verbose_name_plural': '4 - موجودی انبار ها'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'محصول', 'verbose_name_plural': '2 - محصولات'},
        ),
        migrations.AlterModelOptions(
            name='store',
            options={'verbose_name': 'انبار', 'verbose_name_plural': '3 - انبار ها'},
        ),
        migrations.AlterModelOptions(
            name='unit',
            options={'verbose_name': 'واحد اندازه گیری', 'verbose_name_plural': '1 - واحد های اندازه گیری'},
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='1.jpg', upload_to='images/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
