from django.contrib import admin
from django.urls import path, include
from .views import index, galeria, registro, reserva, quienes, local, login, producto,cerrar_sesion, lista_insumos,eliminar,busqueda_mod,modificar

urlpatterns = [
    path('',index,name='index'),
    path('reserva/',reserva,name='reserva'),
    path('galeria/',galeria,name='galeria'),
    path('quienes_somos/',quienes,name='quienes'),
    path('locales/',local,name='locales'),
    path('registro/',registro,name='registro'),
    path('inicio_sesion/',login,name='login'),
    path('insumos/',producto,name='producto'),
    path('cerrar_sesion/' ,cerrar_sesion,name='LOGOUT'),
    path('lista_insumos/',lista_insumos,name='LISTAINSUMO'),
    path('eliminar/<id>/',eliminar,name='ELIMINAR'),
    path('buscar/<id>/',busqueda_mod,name='BUSCAR'),
    path('modificar/',modificar,name='MODIFICAR'),
]
