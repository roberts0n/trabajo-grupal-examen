from django.db import models

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre



class Plataforma(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    




class Juego (models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='juegos/')
    descripcion = models.CharField(max_length=1000)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre



