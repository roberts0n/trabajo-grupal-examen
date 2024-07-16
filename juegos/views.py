from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Juego
from .forms import JuegoForm

# Create your views here.

@login_required
def add_juego(request):
    if request.method == 'POST':
        form = JuegoForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('Home')
    else:
        form = JuegoForm()
        return render(request,'crud/add_juego.html',{'form':form})

def editar_juego(request, juego_id):
    juego = get_object_or_404(Juego,id=juego_id)
    if request.method == 'POST':
        form = JuegoForm(request.POST,request.FILES, instance=juego)
        if form.is_valid():
            form.save()
            return redirect('Home')
    else:
        form = JuegoForm(instance=juego)
    return render(request,'crud/edit_juego.html',{'form':form,'juego':juego})
