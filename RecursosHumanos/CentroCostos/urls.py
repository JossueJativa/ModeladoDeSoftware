from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('pushCentroCostos', views.pushCentroCostos, name='pushCentroCostos'),
    path('agregar',views.agregar, name='agregar'),
    path('elimAtributo/<str:id>/<str:descripcion>',views.elimAtributo, name='elimAtributo'),
    path('edit/<str:id>',views.edit, name='edit'),
    path('editCentroCostos/<str:id>',views.editCentroCostos, name='editCentroCostos'),
    path('search', views.search, name='search'),
    path('PagCentroCostos', views.PagCentroCostos, name='PagCentroCostos'),
    path('PagMovimientoPlanilla', views.PagMovimientoPlanilla, name='PagMovimientoPlanilla'),
    path('PagMovimientoPlanillaSearch', views.PagMovimientoPlanillaSearch, name='PagMovimientoPlanillaSearch'),
    path('PagMovimientoPlanillaEdit/<str:id>', views.PagMovimientoPlanillaEdit, name='PagMovimientoPlanillaEdit'),
]