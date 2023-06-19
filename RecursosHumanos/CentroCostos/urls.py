from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('pushCentroCostos', views.pushCentroCostos, name='pushCentroCostos'),
    path('agregar',views.agregar, name='agregar'),
    path('eliminar/<str:id>/<str:descripcion>',views.eliminar, name='eliminar'),
]