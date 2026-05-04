from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_emprendimiento, name='crear_emprendimiento'),
    path('listar/', views.listar_emprendimientos, name='listar_emprendimientos'),
]