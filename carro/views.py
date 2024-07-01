from django.shortcuts import render,redirect
from .carro import Carro
from juegos.models import Juego
from carro.models import juegoComprado
from django.contrib import messages
from django.utils import timezone

# Create your views here.

def añadirCarrito(request,juego_id):

    carro = Carro(request)

    producto = Juego.objects.get(id=juego_id)

    carro.add(producto=producto)

    return redirect('carro:verCarro')


def eliminarCarrito(request,juego_id):

    carro = Carro(request)

    producto = Juego.objects.get(id=juego_id)

    carro.remove(producto=producto)

    return redirect('verCarro')

def restarCarrito(request,juego_id):

    carro = Carro(request)

    producto = Juego.objects.get(id=juego_id)

    carro.decrement(producto=producto)

    return redirect('carro:verCarro')



def limpiarCarrito(request):

    carro = Carro(request)

    carro.clean()
    messages.success(request, 'Muchas gracias por su compra !')
    return redirect('Home')



def verCarrito(request):
    carro = Carro(request)

    return render(request,'tienda/carro.html',{"carro":carro})


def comprarCarro(request):
    carro = Carro(request)
    usuario = request.user

    for key, value in carro.carro.items():


        juego_id = value['producto_id']
        juego = Juego.objects.get(id=juego_id)
        cantidad = value['cantidad']

        if juego.stock < cantidad :

            return redirect ('carro:verCarro')
    
    juego.stock -= cantidad
    juego.save()

    juego_comprado, created = juegoComprado.objects.get_or_create(
            user=usuario,
            juego=juego,
            defaults={'cantidad': cantidad, 'fecha_compra': timezone.now(),'imagen':juego.imagen.url}
        )

    if not created:
            juego_comprado.cantidad += cantidad
            juego_comprado.save()
    
    carro.clean()
    return redirect('Home')









""" def añadirCarritoDetalle(request,juego_id):

    carro = Carro(request)

    producto = Juego.objects.get(id=juego_id)

    carro.add(producto=producto)

    return redirect('carro:verCarro') """