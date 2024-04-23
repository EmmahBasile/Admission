from django.urls import path
from universities import views

urlpatterns =[
    path("", views.HomeView, name='home'),
    path("login/", views.Login, name='login'),
    path("signup/", views.Signup, name='signup'),
]