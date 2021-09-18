from django.db import models

# Usar foraneas de las tablas de django:
from django.conf import settings
from django.db.models.aggregates import Min
from django.db.models.deletion import CASCADE

# Create your models here.
class HabilidadesUser(models.Model):
    # Atributos de la clase:
    user_habil = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, verbose_name='Usuario', default=1)
    nombre_habil = models.CharField(verbose_name='Nombre de Habilidad', max_length=50)
    porcen_habil = models.IntegerField(verbose_name='Porcentaje de Habilidad', max_length=2, default =0)

    # Clase para los metadatos:
    class Meta:
        verbose_name = 'Habilidad del Usuario'
        verbose_name_plural = 'Habilidades del Usuario'

    # Funcion de string de objeto:
    def __str__(self):
        return self.nombre_habil
    ## Fin de clase Habilidades

class Perfiles(models.Model):
    user_perfil = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, verbose_name='Usuario')
    profesion_user = models.CharField(verbose_name='Profesión', max_length=60)
    perfil_user = models.TextField(verbose_name='Perfil del Usuario')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Modificado el')

    class Meta:
        verbose_name = 'Perfil del Usuario'
        verbose_name_plural = 'Perfil del Usuario'

    def __str__(self) -> str:
        return self.profesion_user



