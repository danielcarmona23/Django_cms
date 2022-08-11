from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import ModelStateFieldsCacheDescriptor

# Create your models here.
class Comentario(models.Model):
    
    nombre = models.CharField(max_length=100, null = False,blank=False)
    correo = models.CharField(max_length=100, null = False,blank=False)
    asunto = models.CharField(max_length=20, null = False,blank=False)
    comentario = models.CharField(max_length=20, null = False,blank=False)

    def __str__(self):
        return "{}-{}-{}-{}-{}".format(self.pk, self.nombre, self.correo, self.comentario, self.asunto)