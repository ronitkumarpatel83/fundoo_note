from django.urls import path
from .views import registration, login, change_password

urlpatterns = [
    path('registration/', registration, name='registration'),
    path('login/', login, name='login'),
    path('change_password/', change_password, name='change_password')
]
