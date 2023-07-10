from django.shortcuts import render

# Create your views here.


# pagina de inicio

def indexView(request):
    return render(request, 'index.html', {})


