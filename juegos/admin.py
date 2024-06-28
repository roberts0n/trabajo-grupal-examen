from django.contrib import admin

from .models import Juego,Plataforma,Categoria

# Register your models here.

admin.site.register(Juego)
admin.site.register(Plataforma)
admin.site.register(Categoria)