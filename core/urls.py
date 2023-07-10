
from django.urls import path, include
from core import views

#app_name = 'core'

urlpatterns = [
    path('', views.indexView, name = 'Pagina Info'),
    path('index/', views.indexView, name = 'index'),
    #include
    path('publicaciones/', include('publicaciones.urls')),
    path('usuarios/', include('usuarios.urls')),
   
]