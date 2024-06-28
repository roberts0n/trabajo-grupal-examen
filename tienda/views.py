from django.shortcuts import render

from juegos.models import Juego,Categoria,Plataforma

# Create your views here.

def home(request):

    juegos = Juego.objects.all()

    return render(request,'tienda/inicio.html',{"juegos":juegos})

def categoria(request):

    return render(request)