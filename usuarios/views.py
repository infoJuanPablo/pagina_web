from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Usuario
#from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrarseForm
from django.urls import reverse
# Create your views here.

# vista basada en clase que crea un usuario

class RegistroView(CreateView):
    model = Usuario
    template_name = 'usuarios/registro.html'
    form_class = RegistrarseForm

    def get_success_url(self):
        return reverse('index')