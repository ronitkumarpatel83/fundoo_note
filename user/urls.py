from django.urls import path
# from .views import registration, login, change_password
from user import views

urlpatterns = [
    # path('registration/', registration, name='registration'),
    # path('login/', login, name='login'),
    # path('change_password/', change_password, name='change_password')
    path('register/', views.RegistrationAPIView.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    path('change_password/', views.ChangePasswordAPIView.as_view()),
]
