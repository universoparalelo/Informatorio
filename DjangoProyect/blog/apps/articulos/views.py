from django.shortcuts import render

# Create your views here.

def Articulo(request):
    return render(request, 'articulos/crearArticulos.html')