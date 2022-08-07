from django.urls import path
from user import views

urlpatterns = [
    path('register/', views.RegistrationAPIView.as_view(), name='registration'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('verify/<str:token>', views.VarifyUser.as_view(), name='token_string')
]
