from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


#clase que crea un formulario
class RegistrarseForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'email', 'telefono', 'domicilio','imagen_perfil','numero_de_tarjeta']

    # cambiar nombre a las etiquetas

        labels = {
        'first_name' : 'ingrese su nombre',
        'last_name' : 'ingrese su apellido',
        'numero_de_tarjeta' : 'Ingrese los 16 Digitos de su Tarjeta'

    }
        
        # tambien podemos agregar calses boostrap con widgets
