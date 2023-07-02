from django.db import models
from django.core.exceptions import ValidationError

class City(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ردیف')
    name = models.CharField(max_length=120, unique=True, verbose_name='نام شهر')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'شهر'
        verbose_name_plural = 'شهر ها'

