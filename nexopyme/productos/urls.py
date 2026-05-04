from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_producto, name='crear_producto'),
    path('listar/', views.listar_productos, name='listar_productos'),
    path('categoria/<str:categoria>/', views.listar_por_categoria, name='listar_por_categoria'),
]