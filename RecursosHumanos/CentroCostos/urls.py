from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('pushCentroCostos', views.pushCentroCostos, name='pushCentroCostos'),
    path('pagCentroCostosadd', views.pagCentroCostosadd, name='pagCentroCostosadd'),
]