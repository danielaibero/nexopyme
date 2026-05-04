from rest_framework import serializers
from .models import Inventario

class InventarioSerializer(serializers.ModelSerializer):
    stock_bajo = serializers.SerializerMethodField()

    class Meta:
        model = Inventario
        fields = ['id', 'producto', 'cantidad_disponible', 
                  'cantidad_minima', 'ultima_actualizacion', 'stock_bajo']
        read_only_fields = ['ultima_actualizacion']

    def get_stock_bajo(self, obj):
        return obj.stock_bajo()