from django import forms
from .models import Juego

class JuegoForm(forms.ModelForm):
    class Meta:
        model = Juego
        fields = ['nombre','precio','imagen','descripcion','categoria','plataforma','stock']
        labels = {
            'nombre': 'Titulo del juego',
        }
