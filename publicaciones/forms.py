from django import forms
from .models import Publicaciones

class CrearPublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicaciones
        fields = ['categoria', 'titulo', 'post']
        labels = {
            'post' : '',
            'titulo': '',
            'categoria': ''

            
        }

        widgets = {
            'titulo': forms.TextInput(attrs= {'placeholder': 'Escribi un Titulo', 'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class' : 'form-select', 'placeholder': 'Categoria'}),
            'post': forms.TextInput(attrs= {'placeholder': '¿En que pesas?', 'class' : 'form-control'})
        }
