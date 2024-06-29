from django.shortcuts import render,redirect
from .carro import Carro
from juegos.models import Juego

# Create your views here.

def añadirCarrito(request,juego_id):

    carro = Carro(request)

    producto = Juego.objects.get(id=juego_id)

    carro.add(producto=producto)

    return redirect('Home')

def eliminarCarrito(request,juego_id):

    carro = Carro(request)

    producto = Juego.objects.get(id=juego_id)

    carro.remove(producto=producto)

    return redirect('Home')

def restarCarrito(request,juego_id):

    carro = Carro(request)

    producto = Juego.objects.get(id=juego_id)

    carro.decrement(producto=producto)

    return redirect('Home')


def limpiarCarrito(request,juego_id):

    carro = Carro(request)

    carro.clean()
    return redirect('Home')

def verCarrito(request):
    carro = Carro(request)

    return render(request,'tienda/carro.html',{"carro":carro})