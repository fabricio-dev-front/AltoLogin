from django.urls import path,include
from . import views
from rest_framework import routers
from usuario.api import viewsets as userviewsets

route = routers.DefaultRouter()
route.register(r'profile', userviewsets.UsuarioViewSet, basename='Profile')


urlpatterns = [
    path('', views.HomePage, name='HomePage'),
    path('login/', views.LoginPage, name='LoginPage'),
    path('register/', views.RegisterPage, name='RegisterPage'),
    path('', include(route.urls))
]
