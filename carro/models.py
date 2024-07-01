from django.db import models
from juegos.models import Juego
from django.contrib.auth.models import User


# Create your models here.

class juegoComprado(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    juego = models.ForeignKey(Juego,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='juegos_comprados',null=True,blank=True)
    cantidad = models.IntegerField()
    fecha_compra = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        fecha = self.fecha_compra.strftime("%d %b %Y %H:%M")
        return f"el usuario {self.user.username} compro {self.cantidad} copias de {self.juego} - a las {fecha}"
    

