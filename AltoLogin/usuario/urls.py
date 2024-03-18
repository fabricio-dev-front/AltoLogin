from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='HomePage'),
    #path('login/', views.LoginPage, name='LoginPage'),
    #path('register/', views.RegisterPage, name='RegisterPage'),
]
