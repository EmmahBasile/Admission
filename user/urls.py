from django.urls import path
from user import views


urlpatterns = [
    path('', views.Sign_upview, name='home'),
    path('login/', views.LoginView, name='login'),

]