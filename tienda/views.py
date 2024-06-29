from django.shortcuts import render, get_object_or_404

from juegos.models import Juego,Categoria,Plataforma

# Create your views here.

def home(request):

    juegos = Juego.objects.all()

    return render(request,'tienda/inicio.html',{"juegos":juegos})

def categoriaSteam(request):

    juegos = Juego.objects.filter(plataforma__nombre="Steam")
    

    return render(request,'tienda/categorias.html',{"juegos":juegos})


def detalleJuego(request, juego_id):
    juego = get_object_or_404(Juego,pk=juego_id)

    return render(request,'tienda/detalle.html',{"juego_detalle":juego})