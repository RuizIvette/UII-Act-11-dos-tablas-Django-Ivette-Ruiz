from django.urls import path
from . import views

app_name = 'app_petco'

urlpatterns = [
    # URLs para Mascotas
    path('', views.listar_mascotas, name='listar_mascotas'), # Ruta principal mostrará mascotas
    path('mascotas/', views.listar_mascotas, name='listar_mascotas'),
    path('mascotas/<int:id_mascota>/', views.detalle_mascota, name='detalle_mascota'),
    path('mascotas/crear/', views.crear_mascota, name='crear_mascota'),
    path('mascotas/editar/<int:id_mascota>/', views.editar_mascota, name='editar_mascota'),
    path('mascotas/borrar/<int:id_mascota>/', views.borrar_mascota, name='borrar_mascota'),

    # URLs para Clientes
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('clientes/<int:id_cliente>/', views.detalle_cliente, name='detalle_cliente'),
    path('clientes/crear/', views.crear_cliente, name='crear_cliente'),
    path('clientes/editar/<int:id_cliente>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/borrar/<int:id_cliente>/', views.borrar_cliente, name='borrar_cliente'),
]