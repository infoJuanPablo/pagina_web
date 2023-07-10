from typing import Any
from django.shortcuts import render
from publicaciones.models import Publicaciones
from django.views.generic import ListView, CreateView
from .forms import CrearPublicacionForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
# pagina de publicaciones


'''# vista basada en funciones
def publicacionesView(request):
    ctx = {
        'posteos' : Publicaciones.objects.all().order_by('fecha')
    }
    return render(request, "publicaciones.html", ctx)'''



# vista basada en clase
class VerPublicaciones(ListView):
    model = Publicaciones
    template_name = 'publicaciones/publicaciones.html'
    context_object_name = 'posteos'
    #ordenar por fecha
    def get_queryset(self):
        consulta_anterior = super().get_queryset()
        return consulta_anterior.order_by('fecha')
    

class Postear(LoginRequiredMixin, CreateView):
    model = Publicaciones
    template_name = 'publicaciones/postear.html'
    form_class = CrearPublicacionForm


    def get_success_url(self):
        return reverse('publicaciones:publicaciones')
