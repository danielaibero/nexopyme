from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    es_emprendedor = models.BooleanField(default=False)
    telefono = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return self.email