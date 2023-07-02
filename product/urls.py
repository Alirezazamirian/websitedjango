from django.urls import path
from .views import Index, OrderSubmit

app_name = 'product'
urlpatterns = [
    path('', Index, name='index'),
    path('order/<int:inventoryid>/', OrderSubmit, name='order'),
]
