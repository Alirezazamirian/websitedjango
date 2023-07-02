from django.contrib import admin
from .models import City

class CityAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('name',)
    ordering = ('name',)

admin.site.register(City, CityAdmin)

