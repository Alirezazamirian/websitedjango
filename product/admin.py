from django.contrib import admin
from .models import Unit, Product, Store, Inventory, Order
from .forms import ProductForm, InventoryForm, OrderSubmitForm

class UnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('id',)

admin.site.register(Unit, UnitAdmin)

#___________________________________________

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price_formatted', 'quantity', 'type', 'admin_photo')
    ordering = ('id',)
    readonly_fields = ('admin_photo',)
    form = ProductForm

admin.site.register(Product, ProductAdmin)

#___________________________________________

class StoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city')
    ordering = ('id',)

admin.site.register(Store, StoreAdmin)

#___________________________________________

class InventoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'store', 'quantity')
    ordering = ('id',)
    form = InventoryForm

admin.site.register(Inventory, InventoryAdmin)

#___________________________________________

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','user' ,'product', 'store', 'quantity', 'condition')
    ordering = ('id',)
    form = OrderSubmitForm

admin.site.register(Order, OrderAdmin)