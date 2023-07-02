from django.db import models
from django.contrib.auth.models import User
from city.models import City

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='شهر محل سکونت')

    def __str__(self):
        return self.city.name



