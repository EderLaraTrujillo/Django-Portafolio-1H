from django.contrib import admin

# Register your models here.
from .models import HabilidadesUser, Perfiles

# Matriculo en el módulo de DjangoAdmin:
admin.site.register(HabilidadesUser)

admin.site.register(Perfiles)