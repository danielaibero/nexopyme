from django.urls import path
from . import views

urlpatterns = [
    path('ver/', views.ver_inventario, name='ver_inventario'),
    path('actualizar/<int:producto_id>/', views.actualizar_inventario, name='actualizar_inventario'),
]