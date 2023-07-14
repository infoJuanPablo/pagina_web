from typing import Any, Dict
from django.shortcuts import render
from publicaciones.models import Publicaciones
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import CrearPublicacionForm, ComentarioForm
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
    


# view que crea posteos
class Postear(LoginRequiredMixin, CreateView):
    model = Publicaciones
    template_name = 'publicaciones/postear.html'
    form_class = CrearPublicacionForm


    def get_success_url(self):
        return reverse('publicaciones:publicaciones')
    
    def form_valid(self, form):
        f = form.save(commit= False)        # con evito que guarde el formulario antes de guardar
        f.creador_id = self.request.user.id
        return super().form_valid(f)



# view que modifica posteos
class EditarPost(LoginRequiredMixin, UpdateView):
    model = Publicaciones
    template_name = 'publicaciones/editar-post.html'
    form_class = CrearPublicacionForm


    def get_success_url(self):
        return reverse('publicaciones:publicaciones')
    

# view que elimina publicacion

class EliminarPost(LoginRequiredMixin,DeleteView):
    model = Publicaciones
    template_name = 'publicaciones/eliminar-post.html'
    
    def get_success_url(self):
        return reverse('publicaciones:publicaciones')
    
    

class PostDetalle(DetailView):
    template_name = 'publicaciones/detalle-post.html'
    model = Publicaciones
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formulario_comentario'] = ComentarioForm()
        return context