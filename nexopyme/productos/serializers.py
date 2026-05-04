from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'emprendimiento', 'nombre', 'descripcion', 
                  'precio', 'categoria', 'stock', 'imagen', 
                  'disponible', 'fecha_creacion']
        read_only_fields = ['fecha_creacion']