from django.db import models
from city.models import City
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

# واحد های اندازه گیری محصولات
class Unit(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ردیف')
    name = models.CharField(max_length=120, unique=True, verbose_name='واحد اندازه گیری')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'واحد اندازه گیری'
        verbose_name_plural = '1 - واحد های اندازه گیری'

#___________________________________________

# محصولات به همراه موجودی کل آنها
class Product(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ردیف')
    name = models.CharField(max_length=120, unique=True, verbose_name='نام محصول')
    price = models.PositiveBigIntegerField(verbose_name='قیمت محصول')
    quantity = models.PositiveIntegerField(verbose_name='تعداد محصول')
    type = models.ForeignKey(Unit, related_name='product_unit',on_delete=models.CASCADE ,verbose_name='واحد اندازه گیری')
    image = models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name='تصویر')

    def __str__(self):
        return self.name

    def price_formatted(self):
        return f'{self.price:,}'
    price_formatted.short_description = 'قیمت'

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))

    admin_photo.short_description = 'تصویر'
    admin_photo.allow_tags = True

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = '2 - محصولات'

#___________________________________________

# تمامی انبار های موجود در شهر ها
class Store(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ردیف')
    name = models.CharField(max_length=120, unique=True, verbose_name='نام انبار')
    city = models.ForeignKey(City, related_name='store_city',on_delete=models.CASCADE ,verbose_name='شهر انبار')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'انبار'
        verbose_name_plural = '3 - انبار ها'

#___________________________________________

# موجودی هر انبار
class Inventory(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ردیف')
    product = models.ForeignKey(Product, related_name='inventory_product',on_delete=models.CASCADE ,verbose_name='محصول مورد نظر')
    store = models.ForeignKey(Store, related_name='incentory_store', on_delete=models.CASCADE, verbose_name='انبار مورد نظر')
    quantity = models.PositiveIntegerField(verbose_name='موجودی این انبار')

    def __str__(self):
        return f'{self.store} - {self.product}'

    class Meta:
        verbose_name = 'موجودی انبار'
        verbose_name_plural = '4 - موجودی انبار ها'
        #برای اینکه یک انبار به همراه یک محصول دوبار تکرار نشود
        unique_together = [("product", "store")]

# سفارشات
class Order(models.Model):
    STATUS = (
        ('pending', 'در انتظار'),
        ('failed', 'رد شده'),
        ('confirmed', 'تایید شده'),
    )
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ردیف')
    user = models.ForeignKey(User, related_name='order_user',on_delete=models.CASCADE ,verbose_name='کاربر')
    product = models.ForeignKey(Product, related_name='order_product',on_delete=models.CASCADE ,verbose_name='محصول')
    store = models.ForeignKey(Store, related_name='order_store', on_delete=models.CASCADE, verbose_name='انبار')
    quantity = models.PositiveIntegerField(verbose_name='تعداد')
    condition = models.CharField(max_length=20, choices=STATUS, verbose_name='وضعیت سفارش')

    def __str__(self):
        return f'{self.user} - {self.product}'

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = '5 - سفارشات'