from rest_framework import serializers
from .models import Emprendimiento

class EmprendimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprendimiento
        fields = ['id', 'usuario', 'nombre_negocio', 'descripcion', 
                  'categoria', 'ubicacion', 'imagen', 'fecha_creacion']
        read_only_fields = ['usuario', 'fecha_creacion']