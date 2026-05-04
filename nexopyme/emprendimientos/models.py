from django.db import models
from usuarios.models import Usuario

class Emprendimiento(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    nombre_negocio = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    categoria = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=100, blank=True)
    imagen = models.ImageField(upload_to='emprendimientos/', blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_negocio