# Generated by Django 4.2.2 on 2023-06-19 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0002_alter_city_options_alter_city_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ردیف'),
        ),
    ]
