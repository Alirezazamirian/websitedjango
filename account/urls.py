from django.urls import path
from .views import login_page,register_page

app_name = 'account'
urlpatterns = [
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
]
