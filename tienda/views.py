from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,authenticate,login
from juegos.models import Juego,Categoria,Plataforma
from .forms import CustomUserCreationForm


# Create your views here.


def home(request):

    juegos = Juego.objects.all()

    return render(request,'tienda/inicio.html',{"juegos":juegos})

def categoriaSteam(request):

    juegos = Juego.objects.filter(plataforma__nombre="Steam")
    plataforma = "Plataforma : Steam"
    

    return render(request,'tienda/filtrado.html',{"juegos":juegos,"titulo":plataforma})

def categoriaSwitch(request):

    juegos = Juego.objects.filter(plataforma__nombre="Switch")
    plataforma = "Plataforma : Switch"
    

    return render(request,'tienda/filtrado.html',{"juegos":juegos,"titulo":plataforma})

def categoriaXbox(request):

    juegos = Juego.objects.filter(plataforma__nombre="Xbox")
    plataforma = "Plataforma : Xbox"
    

    return render(request,'tienda/filtrado.html',{"juegos":juegos,"titulo":plataforma})

def categoriaPlay(request):

    juegos = Juego.objects.filter(plataforma__nombre="Playstation")
    plataforma = "Plataforma : Playstation"
    

    return render(request,'tienda/filtrado.html',{"juegos":juegos,"titulo":plataforma})

def categoriaRpg(request):

    juegos = Juego.objects.filter(categoria__nombre="RPG")
    plataforma = "Categoria : RPG"
    

    return render(request,'tienda/filtrado.html',{"juegos":juegos,"titulo":plataforma})

def categoriaAccion(request):

    juegos = Juego.objects.filter(categoria__nombre="Acción")
    plataforma = "Categoria : Acción"
    

    return render(request,'tienda/filtrado.html',{"juegos":juegos,"titulo":plataforma})


def categoriaDeportes(request):

    juegos = Juego.objects.filter(categoria__nombre="Deportes")
    plataforma = "Categoria : Deportes"
    

    return render(request,'tienda/filtrado.html',{"juegos":juegos,"titulo":plataforma})


@login_required
def detalleJuego(request, juego_id):
    juego = get_object_or_404(Juego,pk=juego_id)

    return render(request,'tienda/detalle.html',{"juego_detalle":juego})
def exit(request):

    logout(request)
    
    return redirect('Home')

def register(request):

    data = {
        'form' : CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('Home')
    
    return render(request,'registration/register.html',data)
