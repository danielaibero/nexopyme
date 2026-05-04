from django.db import models
from productos.models import Producto

class Inventario(models.Model):
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE)
    cantidad_disponible = models.IntegerField(default=0)
    cantidad_minima = models.IntegerField(default=5)
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Inventario de {self.producto.nombre}"
    
    def stock_bajo(self):
        return self.cantidad_disponible <= self.cantidad_minima