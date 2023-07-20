from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Usuario
#from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrarseForm
from django.urls import reverse
from django.contrib.auth import login
# Create your views here.

# vista basada en clase que crea un usuario

class RegistroView(CreateView):
    model = Usuario
    template_name = 'usuarios/registro.html'
    form_class = RegistrarseForm

    def get_success_url(self):
        return reverse('index')
    
    def form_valid(self, form):
        respuesta = super().form_valid(form)        # respuesta es algo que ya retornaba la funcion
        usuario = form.save()
        login(self.request, usuario)
        return respuesta