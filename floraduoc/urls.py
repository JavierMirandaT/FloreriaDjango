from django.urls import path
from .views import donaciones, index, usuario, tienda, agregar_flora, listar_floras, modificar_floras, eliminar_floras


urlpatterns = [
    path('', index , name="index"),
    path('donaciones', donaciones, name="donaciones"),
    path('usuario', usuario,name="usuario"),
    path('tienda', tienda,name="tienda"),
    path('index', index , name="Inicio"),
    path('agregar', agregar_flora , name="agregar_flora"),
    path('listar', listar_floras , name="listar_floras"),
    path('modificar/<id>/', modificar_floras , name="modificar_floras"),
    path('eliminar/<id>/', eliminar_floras , name="eliminar_floras"),
]
