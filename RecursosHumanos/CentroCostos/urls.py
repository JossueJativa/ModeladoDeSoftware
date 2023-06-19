from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('table', views.tables, name='table'),
    path('get_usuarios', views.get_usuarios, name='get_usuarios'),
]