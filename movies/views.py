from django.shortcuts import render
from .models import Movies

def index(request):
    peliculas = Movies.objects.all()
    return render(request, 'index.html', {
        'peliculas': peliculas
    })

def pelicula_details(request, identification):
    pelicula_obj = Movies.objects.get(identification=identification)
    return render(request, 'pelicula_details.html', {
        'pelicula': pelicula_obj
    } )